import openapi_parser.specification

from jubladb_api.metamodel import classes

DATA_TYPE_MAP: dict[tuple[openapi_parser.specification.DataType, openapi_parser.specification.StringFormat|openapi_parser.specification.NumberFormat|openapi_parser.specification.IntegerFormat|None], classes.AttributeType] = {
    (openapi_parser.specification.DataType.INTEGER, None): classes.AttributeType.INTEGER,
    (openapi_parser.specification.DataType.BOOLEAN, None): classes.AttributeType.BOOLEAN,
    (openapi_parser.specification.DataType.NUMBER, None): classes.AttributeType.FLOAT,
    (openapi_parser.specification.DataType.STRING, None): classes.AttributeType.STRING,
    (openapi_parser.specification.DataType.STRING, openapi_parser.specification.StringFormat.DATE): classes.AttributeType.DATE,
    (openapi_parser.specification.DataType.STRING, openapi_parser.specification.StringFormat.TIME): classes.AttributeType.TIME,
    (openapi_parser.specification.DataType.STRING, openapi_parser.specification.StringFormat.DATETIME): classes.AttributeType.DATETIME,
}

OPERATIONS_MAP: dict[tuple[bool, openapi_parser.specification.OperationMethod], classes.Operation] = {
    (True, openapi_parser.specification.OperationMethod.GET): classes.Operation.GetList,
    (False, openapi_parser.specification.OperationMethod.GET): classes.Operation.GetSingle,
    (False, openapi_parser.specification.OperationMethod.PUT): classes.Operation.CreateSingle,
    (False, openapi_parser.specification.OperationMethod.PATCH): classes.Operation.UpdateSingle,
    (False, openapi_parser.specification.OperationMethod.DELETE): classes.Operation.DeleteSingle,
}

PLURAL_SINGULAR_CONVERSION: list[tuple[str, str]] = [
    ("people", "person"),
    ("addresses", "address"),
    ("ies", "y"),
    ("s", ""),
]

PLURAL_SINGULAR_SPECIAL_CASES = {
    "people": "person",
    "addresses": "person",
}

def pretty_repr(x: object, indent=1) -> str:
    if isinstance(x, dict):
        res = "{\n"
        for (key, value) in x.items():
            res += f"{'    ' * indent}{pretty_repr(key, indent+1)}: {pretty_repr(value, indent + 1)},\n"
        res += "}"
        return res
    elif isinstance(x, list):
        res = "[\n"
        for item in x:
            res += f"{'    '*indent}{pretty_repr(item, indent+1)},\n"
        res += "]"
        return res
    else:
        return repr(x)

def get_singular_name(plural: str) -> str:
    for (ending, replacement) in PLURAL_SINGULAR_CONVERSION:
        if plural.endswith(ending):
            return plural[:-len(ending)] + replacement
    print(f"WARNING: Cannot get singular name for {plural}")
    return plural

def generate_metamodel(spec: openapi_parser.specification.Specification) -> list[classes.Entity]:
    entities: list[classes.Entity] = []
    spec_types: openapi_parser.specification.String = spec.schemas["types"]
    for entity_type in spec_types.enum:
        schema: openapi_parser.specification.Object = spec.schemas[entity_type]
        base_url = f"/api/{entity_type}"
        spec_paths = {p.url: p for p in spec.paths if p.url.startswith(base_url)}
        spec_path_list = spec_paths.get(base_url, None)
        spec_path_single = spec_paths.get(f"{base_url}/{{id}}", None)
        spec_operations: dict[tuple[bool, openapi_parser.specification.OperationMethod], openapi_parser.specification.Operation] = {}

        if spec_path_list is not None:
            for op in spec_path_list.operations:
                spec_operations[(True, op.method)] = op
        if spec_path_single is not None:
            for op in spec_path_single.operations:
                spec_operations[(False, op.method)] = op

        sort_attrs: set[str] = set()
        attr_filters: dict[str, set[str]] = {}

        name = entity_type.replace("-", "_")
        entity = classes.Entity(url=base_url if base_url in spec_paths else "",
                                                      name_singular=get_singular_name(name),
                                                      name_plural=name,
                                                      )
        entities.append(entity)

        for op_key, op in spec_operations.items():
            if op_key in OPERATIONS_MAP:
                entity.allowed_operations.add(OPERATIONS_MAP[op_key])
            if op_key == (True, openapi_parser.specification.OperationMethod.GET):
                try:
                    include_param = next(p for p in op.parameters if p.name=="include").schema
                except StopIteration:
                    pass
                else:
                    assert include_param.type == openapi_parser.specification.DataType.ARRAY
                    include_param: openapi_parser.specification.Array
                    entity.includeable.extend(include_param.items.enum)

                try:
                    sort_param = next(p for p in op.parameters if p.name=="sort").schema
                except StopIteration:
                    pass
                else:
                    assert sort_param.type == openapi_parser.specification.DataType.ARRAY
                    sort_param: openapi_parser.specification.Array
                    sort_attrs = set(sort_param.items.enum)

                for p in op.parameters:
                    if not p.name.startswith("filter["):
                        continue
                    a = len("filter[")
                    b = p.name.index("]", a)
                    c = p.name.index("[", b)+1
                    d = p.name.index("]", c)
                    attr_name = p.name[a:b]
                    filter_type = p.name[c:d]
                    attr_filters.setdefault(attr_name, set()).add(filter_type)

        for prop in schema.properties:
            type_ = DATA_TYPE_MAP.get((prop.schema.type, getattr(prop.schema, "format", None)), None)
            if type_ is None:
                print(f"Unknown type {prop.schema.type} for property {entity_type}.{prop.name}")
                continue
            attr = classes.Attribute(name=prop.name,
                                                           type_=type_,
                                                           sortable=prop.name in sort_attrs,
                                                           filter_types=attr_filters.get(prop.name, set()),
                                                           )
            entity.attributes.append(attr)

    with open("../jubladb_api/metamodel/model.py", "w") as f:
        f.write(f"""# This file is auto-generated by generate_metamodel.py
from jubladb_api.metamodel.classes import *
import typing

ENTITIES = {pretty_repr({e.name_singular: e for e in entities})}

EntityName = typing.Literal[{', '.join(f'"{e.name_singular}"' for e in entities)}]
""")
    return entities

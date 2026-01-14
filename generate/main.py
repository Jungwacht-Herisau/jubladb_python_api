#!/usr/bin/env python3
import pathlib
import pickle
import sys

from openapi_parser.specification import Specification

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import shutil
import aenum
import openapi_parser
import openapi_parser.specification
import requests
import tqdm

import templates
import jubladb_api.core.metamodel_classes as classes

SPEC_FILE_NAME = pathlib.Path(__file__).parent.parent / "spec.yaml"
MODULE_NAME = "jubladb_api"


def download_spec():
    response = requests.get("https://db.jubla.ch/api/openapi.yaml", stream=True)
    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024
    with tqdm.tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
        with open(SPEC_FILE_NAME, "wb") as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        if total_size != 0 and progress_bar.n != total_size:
            raise RuntimeError("Could not download spec file")


def patch_openapi_parser():
    aenum.extend_enum(openapi_parser.parser.ContentType, "JSON_API", "application/vnd.api+json")
    aenum.extend_enum(openapi_parser.parser.StringFormat, "URI_REFERENCE", "uri-reference")


DATA_TYPE_MAP: dict[tuple[openapi_parser.specification.DataType, openapi_parser.specification.StringFormat | openapi_parser.specification.NumberFormat | openapi_parser.specification.IntegerFormat | None], classes.AttributeType] = {
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

"""
(ending, replacement)
"""
PLURAL_SINGULAR_CONVERSION: list[tuple[str, str]] = [
    ("people", "person"),
    ("addresses", "address"),
    ("ies", "y"),
    ("s", ""),
]

"""
(entity_type, relation_name): related_entity_type
"""
RELATION_TYPES: dict[tuple[str, str], str] = {
    ("course", "contact"): "person",
    ("course", "kind"): "event_kind",  # unsure if this is correct, because with the current API I don't see a way how to retrieve any course
    ("course", "dates"): "date",
    ("course", "leaders"): "person",
    ("date", "event"): "event",
    ("event_kind", "kind_category"): "event_kind_category",
    ("event", "contact"): "person",
    ("event", "kind"): "event_kind",
    ("event", "dates"): "date",
    ("group", "contact"): "person",
    ("group", "creator"): "person",
    ("group", "updater"): "person",
    ("group", "deleter"): "person",
    ("group", "parent"): "group",
    ("group", "layer_group"): "group",
    ("group", "phone_numbers"): "phone_number",
    ("group", "social_accounts"): "social_account",
    ("group", "additional_emails"): "additional_email",
    ("invoice_item", "invoice"): "invoice",
    ("invoice", "group"): "group",
    ("invoice", "recipient"): "person",
    ("invoice", "invoice_items"): "invoice_item",
    ("person", "primary_group"): "group",
    ("person", "layer_group"): "group",
    ("person", "roles"): "role",
    ("person", "phone_numbers"): "phone_number",
    ("person", "social_accounts"): "social_account",
    ("person", "additional_emails"): "additional_email",
    ("role", "person"): "person",
    ("role", "group"): "group",
    ("role", "layer_group"): "group",
    ("group", "mailing_lists"): "mailing_list",
    ("mailing_list", "group"): "group",
}

OPTIONAL_ATTRIBUTES: set[tuple[str, str]] = {
    ("group", "archived_at"),
    ("group", "deleted_at"),
    ("group", "logo"),
    ("role", "label"),
    ("role", "end_on"),
    ("group", "email"),
    ("group", "zip_code"),
    ("group", "self_registration_url"),
    ("group", "logo"),
    ("group", "privacy_policies"),
    ("event", "type"),
    ("event", "kind_id"),
    ("event", "application_opening_at"),
    ("event", "application_closing_at"),
    ("event", "application_contact_id"),
    ("event", "external_application_link"),
    ("event", "maximum_participants"),
    ("person", "company_name"),
    ("person", "address_care_of"),
    ("person", "postbox"),
    ("person", "additional_information"),
    ("person", "nickname"),
    ("person", "email"),
    # this info isn't documented anywhere, so there are probably more
}

# (entity_name, attribute_name): singular_attribute_name
ARRAY_ATTRIBUTES: dict[tuple[str, str], str] = {
    ("event", "group_ids"): "group_id",
}

STRING_REPRESENTATION_ATTRIBUTES: dict[str, list[str]] = {
    "additional_address": ["contactable_id", "street", "housenumber", "zip_code", "town"],
    "additional_email": ["contactable_id", "email"],
    "course": ["name"],
    "date": ["event_id", "start_at", "end_at"],
    "event_kind_category": ["label"],
    "event_kind": ["label"],
    "event": ["name"],
    "group": ["name"],
    "invoice_item": ["invoice_id", "name"],
    "invoice": ["title"],
    "mailing_list": ["name"],
    "person_name": ["first_name", "last_name"],
    "person": ["first_name", "last_name"],
    "phone_number": ["contactable_id", "number"],
    "role": ["person_id", "group_id", "type"],
    "self_registration": ["first_name", "last_name"],
    "social_account": ["contactable_id", "name"],
}

README_MD_URL = "https://raw.githubusercontent.com/hitobito/hitobito_jubla/refs/heads/master/README.md"
ROLES_START = "<!-- roles:start -->"
ROLES_END = "<!-- roles:end -->"


def pretty_repr(x: object, indent=1) -> str:
    if isinstance(x, dict):
        res = "{\n"
        for (key, value) in x.items():
            res += f"{'    ' * indent}{pretty_repr(key, indent + 1)}: {pretty_repr(value, indent + 1)},\n"
        res += "}"
        return res
    elif isinstance(x, list):
        res = "[\n"
        for item in x:
            res += f"{'    ' * indent}{pretty_repr(item, indent + 1)},\n"
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


def _generate_api_info(spec: openapi_parser.specification.Specification) -> classes.APIInfo:
    default_server_url = ""
    for srv in spec.servers:
        default_server_url = srv.url
        break

    return classes.APIInfo(
        version=spec.info.version,
        auth_header=_get_auth_header_name(spec),
        default_server_url=default_server_url,
    )


def _get_auth_header_name(spec: Specification) -> str:
    auth_header = ""
    for sschema in spec.security_schemas.values():
        if sschema.type == openapi_parser.specification.SecurityType.API_KEY and sschema.location == openapi_parser.specification.BaseLocation.HEADER:
            auth_header = sschema.name
    return auth_header


class CodeGenerator(object):
    def __init__(self, spec: openapi_parser.specification.Specification):
        self.spec = spec
        self.output_dir = pathlib.Path(__file__).parent / ".." / "src" / MODULE_NAME / "generated"
        self.generator = templates.TemplatedGenerator()

    def cleanup(self):
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir, ignore_errors=True)
        self.output_dir.mkdir(parents=True)

    def _generate_metamodel(self):
        entities: list[classes.Entity] = []
        spec_types: openapi_parser.specification.String = self.spec.schemas["types"]
        for entity_type in spec_types.enum:
            schema: openapi_parser.specification.Object = self.spec.schemas[entity_type]
            base_url = f"/api/{entity_type}"
            spec_paths = {p.url: p for p in self.spec.paths if p.url.startswith(base_url)}
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
            attr_filters: dict[str, list[str]] = {}

            name = entity_type.replace("-", "_")
            singular_name = get_singular_name(name)
            entity = classes.Entity(url=base_url if base_url in spec_paths else "",
                                    name_singular=singular_name,
                                    name_plural=name,
                                    string_representation_attributes=STRING_REPRESENTATION_ATTRIBUTES.get(singular_name, []),
                                    )
            entities.append(entity)

            for op_key, op in spec_operations.items():
                if op_key in OPERATIONS_MAP:
                    entity.allowed_operations.append(OPERATIONS_MAP[op_key])
                if op_key == (True, openapi_parser.specification.OperationMethod.GET):
                    try:
                        include_param = next(p for p in op.parameters if p.name == "include").schema
                    except StopIteration:
                        pass
                    else:
                        assert include_param.type == openapi_parser.specification.DataType.ARRAY
                        include_param: openapi_parser.specification.Array
                        entity.includeable.extend(include_param.items.enum)

                    try:
                        sort_param = next(p for p in op.parameters if p.name == "sort").schema
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
                        c = p.name.index("[", b) + 1
                        d = p.name.index("]", c)
                        attr_name = p.name[a:b]
                        filter_type = p.name[c:d]
                        attr_filters.setdefault(attr_name, list()).append(filter_type)

            for prop in schema.properties:
                if prop.schema.type == openapi_parser.specification.DataType.ARRAY:
                    type_ = classes.AttributeType.STRING  # TODO find item type (doesn't seem to be included in spec)
                    is_array = True
                else:
                    type_ = DATA_TYPE_MAP.get((prop.schema.type, getattr(prop.schema, "format", None)), None)
                    is_array = False
                if type_ is None:
                    type_ = DATA_TYPE_MAP.get((prop.schema.type, None), None)
                if type_ is None:
                    print(f"Unknown type {prop.schema.type} for property {entity_type}.{prop.name}")
                    continue
                array_attr_name = ARRAY_ATTRIBUTES.get((entity.name_singular, prop.name), None)
                filter_name = array_attr_name if array_attr_name is not None else prop.name
                filter_types = attr_filters.get(filter_name, list())
                attr = classes.Attribute(name=prop.name,
                                         type_=type_,
                                         array=array_attr_name is not None or is_array,
                                         optional=(entity.name_singular, prop.name) in OPTIONAL_ATTRIBUTES,
                                         sortable=prop.name in sort_attrs,
                                         filter_name=filter_name if filter_types else None,
                                         filter_types=filter_types,
                                         )
                entity.attributes.append(attr)

            related_schema = self.spec.schemas.get(f"{entity_type}_related", None)
            relations_schema = self.spec.schemas.get(f"{entity_type}_relationships", None)
            if ((related_schema is not None and related_schema.type == openapi_parser.specification.DataType.ARRAY)
                    and (relations_schema is not None and relations_schema.type == openapi_parser.specification.DataType.OBJECT)):
                related_schema_array: openapi_parser.specification.Array = related_schema
                relations_schema_object: openapi_parser.specification.Object = relations_schema
                if related_schema_array.items.type == openapi_parser.specification.DataType.STRING:
                    related_schema_items: openapi_parser.specification.String = related_schema_array.items
                    for relation_name in related_schema_items.enum:
                        try:
                            relation_property: openapi_parser.specification.Object = next(p for p in relations_schema_object.properties if p.name == relation_name).schema
                            relation_property_data = next(p for p in relation_property.properties if p.name == "data")
                        except StopIteration:
                            print(f"WARNING: relation {relation_name} not found in {entity_type}_relations")
                            continue
                        try:
                            related_type_singular = RELATION_TYPES[(entity.name_singular, relation_name)]
                        except KeyError:
                            print(f"WARNING: key (\"{entity.name_singular}\", \"{relation_name}\") not found in RELATION_TYPES")
                            continue
                        try:
                            related_type_plural = next(st for st in spec_types.enum if get_singular_name(st) == related_type_singular)
                        except StopIteration:
                            print(f"WARNING: no plural name for {related_type_singular}")
                            continue
                        to_many = relation_property_data.schema.type == openapi_parser.specification.DataType.ARRAY
                        entity.relations.append(classes.RelationType(relation_name, related_type_singular, related_type_plural, to_many))

        api_info = _generate_api_info(self.spec)

        renderer = self.generator.renderer("metamodel.py.jinja2")
        with open(self.output_dir / "metamodel.py", "w") as f:
            f.write(renderer.render({
                "entities": entities,
                "api_info": api_info,
            }))
        return entities

    def _generate_entities(self, entities):
        rendered = self.generator.renderer("__init__.py.jinja2").render({})
        with open(self.output_dir / "__init__.py", "w") as f:
            f.write(rendered)

        datetime_attribute_types = {classes.AttributeType.DATE, classes.AttributeType.TIME, classes.AttributeType.DATETIME}

        (self.output_dir / "entities").mkdir()

        rendered = self.generator.renderer("entities/__init__.py.jinja2").render({"entities": entities})
        with open(self.output_dir / "entities" / "__init__.py", "w") as f:
            f.write(rendered)

        rendered = self.generator.renderer("entities/keys.py.jinja2").render({"entities": entities})
        with open(self.output_dir / "entities" / "keys.py", "w") as f:
            f.write(rendered)

        for entity in entities:
            rendered = self.generator.renderer("entity.py.jinja2").render({
                "entity": entity,
                "need_datetime_import": any(attr.type_ in datetime_attribute_types for attr in entity.attributes),
            })
            with open(self.output_dir / "entities" / f"{entity.name_singular}.py", "w") as f:
                f.write(rendered)

    def _generate_client(self, entities):
        renderer = self.generator.renderer("client.py.jinja2")
        code = renderer.render({
            "entities": entities,
            "api_key_header": _get_auth_header_name(self.spec),
        })
        with open(self.output_dir / "client.py", "w") as f:
            f.write(code)

    def _generate_groups_roles(self):
        md = requests.get(README_MD_URL).content.decode("utf-8")
        it = iter(md.splitlines())
        line = next(it, None)
        while line is not None and line != ROLES_START:
            line = next(it, None)
        if line is None:
            raise ValueError(ROLES_START + "not found")
        line = next(it, None)
        base_indent = 4
        last_indent = 0
        indent_step = 2
        name_stack = []
        roles: list[tuple[str, str, list[str], bool]] = []
        groups: dict[str, str] = {}
        while line is not None and line != ROLES_END:
            if line.strip():
                current_indent = ((len(line) - len(line.lstrip())) - base_indent) // indent_step + 1
                stripped: str = line.strip()
                if stripped.startswith("* "):
                    stripped = stripped[len("* "):]
                    name_end = stripped.index(":") if ":" in stripped else len(stripped)
                    name = stripped[:name_end].rstrip(":")
                    if current_indent <= last_indent:
                        for _ in range(last_indent - current_indent + 1):
                            name_stack.pop()
                    name_stack.append(name)
                    if "--" in stripped:
                        dashdash_index = stripped.index("--")
                        requires_2fa = stripped[name_end + 1:dashdash_index].strip().startswith("2FA")
                        rights_str = stripped[name_end + (5 if requires_2fa else 1):dashdash_index].lstrip(" [").rstrip(
                            "] ")
                        rights = [r.strip() for r in rights_str.split(",") if r.strip()]
                        role_id = stripped[dashdash_index + len("--"):].lstrip(" (").rstrip(") ")
                        roles.append((role_id, name, rights, requires_2fa))

                        group_id = role_id.rsplit("::", 1)[0]
                        if group_id not in groups:
                            full_name = " - ".join(
                                v for i, v in enumerate(name_stack[:-1]) if i == 0 or v != name_stack[i - 1])
                            groups[group_id] = full_name

                last_indent = current_indent
            line = next(it, None)

        grouptype_vars: list[tuple[str, str]] = []
        roletype_vars: list[tuple[str, str]] = []
        group_role_vars: list[tuple[str, str]] = []

        group_var_names: dict[str, str] = {}
        role_var_names: dict[str, str] = {}
        role_var_names_by_group_var_name: dict[str, list[str]] = {}

        for group_id, full_name in groups.items():
            var_name = group_id.upper().replace("::", "_")
            group_var_names[group_id] = var_name
            role_var_names_by_group_var_name[var_name] = []
        for role_id, name, rights, requires_2fa in roles:
            var_name = role_id.upper().replace("::", "_").replace("GROUP", "ROLE", 1)
            group_id = role_id.rsplit("::", 1)[0]
            group_var_n = group_var_names[group_id]
            role_var_names_by_group_var_name[group_var_n].append(var_name)
            role_var_names[role_id] = var_name

        for group_id, full_name in groups.items():
            var_name = group_var_names[group_id]
            grouptype_vars.append((var_name, f"GroupType(\"{group_id}\", \"{full_name}\", [])"))

            roles_str = ", ".join(role_var_names_by_group_var_name[var_name])
            group_role_vars.append((var_name, roles_str))

        for role_id, name, rights, requires_2fa in roles:
            var_name = role_var_names[role_id]
            group_id = role_id.rsplit("::", 1)[0]
            group_var_n = group_var_names[group_id]
            rights_str = ", ".join(f"\"{r}\"" for r in rights)
            roletype_vars.append((var_name, f"RoleType(\"{role_id}\", \"{name}\", [{rights_str}], {requires_2fa}, {group_var_n})"))

        renderer = self.generator.renderer("groups_roles.py.jinja2")
        with open(self.output_dir / "groups_roles.py", "w") as f:
            f.write(renderer.render({
                "grouptype_vars": grouptype_vars,
                "roletype_vars": roletype_vars,
                "group_role_vars": group_role_vars,
                "group_var_names": group_var_names,
                "role_var_names": role_var_names,
            }))

    def run(self):
        entities = self._generate_metamodel()
        self._generate_entities(entities)
        self._generate_client(entities)
        self._generate_groups_roles()


if __name__ == '__main__':
    _spec_file_name = pathlib.Path(__file__).parent / "spec.pickle"

    patch_openapi_parser()
    if _spec_file_name.exists():
        print(f"using cached spec from {_spec_file_name}")
        with open(_spec_file_name, "rb") as f:
            _spec = pickle.load(f)
    else:
        download_spec()

        print("Parsing OpenAPI spec... ")
        _spec = openapi_parser.parse(SPEC_FILE_NAME)
        print("Parsed OpenAPI spec successfully.")

        with open(_spec_file_name, "wb") as f:
            pickle.dump(_spec, f)

    generator = CodeGenerator(_spec)
    generator.cleanup()
    generator.run()

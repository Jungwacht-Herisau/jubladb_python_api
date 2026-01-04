import os
import pathlib

import jinja2

import jubladb_api

DATETIME_ATTRIBUTE_TYPES = {jubladb_api.metamodel.AttributeType.DATE, jubladb_api.metamodel.AttributeType.TIME, jubladb_api.metamodel.AttributeType.DATETIME}

ATTR_TYPE_TO_PY_CLASS = {
    jubladb_api.metamodel.AttributeType.INTEGER: "int",
    jubladb_api.metamodel.AttributeType.BOOLEAN: "bool",
    jubladb_api.metamodel.AttributeType.STRING: "str",
    jubladb_api.metamodel.AttributeType.FLOAT: "float",
    jubladb_api.metamodel.AttributeType.DATE: "datetime.date",
    jubladb_api.metamodel.AttributeType.TIME: "datetime.time",
    jubladb_api.metamodel.AttributeType.DATETIME: "datetime.datetime",
}


def snake_case_to_pascal_case(sc: str) -> str:
    words = sc.split("_")
    return "".join(w.title() for w in words)

def attribute_type_to_python_type(attr_type: jubladb_api.metamodel.AttributeType) -> str:
    return ATTR_TYPE_TO_PY_CLASS[attr_type]

def generate_entities(entities: list[jubladb_api.metamodel.Entity]) -> None:
    code_dir = pathlib.Path("jubladb_api/entities")
    for file in os.listdir(code_dir):
        if file.endswith(".py") and not file in {"__init__.py", "base.py"}:
            os.remove(code_dir / file)

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("templates"),
        autoescape=jinja2.select_autoescape(),
    )
    env.filters["snake_case_to_pascal_case"] = snake_case_to_pascal_case
    env.filters["attribute_type_to_python_type"] = attribute_type_to_python_type
    template = env.get_template("entity.py.jinja2")
    for entity in entities:
        rendered = template.render(entity=entity,
                                   need_datetime_import=any(attr.type_ in DATETIME_ATTRIBUTE_TYPES for attr in entity.attributes))
        with open(f"jubladb_api/entities/{entity.name_singular}.py", "w") as f:
            f.write(rendered)
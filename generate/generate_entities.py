import os
import pathlib

import templates

CODE_DIR = pathlib.Path(__file__).parent / "../jubladb_api/entities"

def generate_entities(entities: "list[jubladb_api.metamodel.Entity]") -> None:
    import jubladb_api.metamodel.classes
    datetime_attribute_types = {jubladb_api.metamodel.classes.AttributeType.DATE, jubladb_api.metamodel.classes.AttributeType.TIME, jubladb_api.metamodel.classes.AttributeType.DATETIME}

    entity_generator = templates.TemplatedGenerator("entity.py.jinja2")
    for entity in entities:
        rendered = entity_generator.render({
            "entity": entity,
            "need_datetime_import": any(attr.type_ in datetime_attribute_types for attr in entity.attributes),
        })
        with open(CODE_DIR / f"{entity.name_singular}.py", "w") as f:
            f.write(rendered)

    init_generator = templates.TemplatedGenerator("entity_init.py.jinja2")
    rendered = init_generator.render({"entities": entities})
    with open(CODE_DIR / "__init__.py", "w") as f:
        f.write(rendered)


def cleanup():
    for file in os.listdir(CODE_DIR):
        if file.endswith(".py") and not file in {"base.py", }:
            os.remove(CODE_DIR / file)

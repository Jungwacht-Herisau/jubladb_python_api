import pathlib

import jinja2
import black




def snake_case_to_pascal_case(sc: str) -> str:
    words = sc.split("_")
    return "".join(w.title() for w in words)

def attribute_type_to_python_type(attr_type: "jubladb_api.metamodel.AttributeType") -> str:
    from jubladb_api.metamodel.classes import AttributeType
    attr_type_to_py_class = {
        AttributeType.INTEGER: "int",
        AttributeType.BOOLEAN: "bool",
        AttributeType.STRING: "str",
        AttributeType.FLOAT: "float",
        AttributeType.DATE: "datetime.date",
        AttributeType.TIME: "datetime.time",
        AttributeType.DATETIME: "datetime.datetime",
    }
    return attr_type_to_py_class[attr_type]

def entity_has_sortable_attributes(entity: "jubladb_api.metamodel.classes.Entity") -> bool:
    return any(attr.sortable for attr in entity.attributes)

class TemplatedGenerator(object):
    def __init__(self, template_name: str):
        template_dir =  pathlib.Path(__file__).parent / "templates"
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir),
            autoescape=jinja2.select_autoescape(),
        )
        self.env.filters["snake_case_to_pascal_case"] = snake_case_to_pascal_case
        self.env.filters["attribute_type_to_python_type"] = attribute_type_to_python_type
        self.env.filters["entity_has_sortable_attributes"] = entity_has_sortable_attributes
        self.env.filters["repr"] = repr

        self.template = self.env.get_template(template_name)

    def render(self, context: dict, reformat=True) -> str:
        result = self.template.render(**context)
        if reformat:
            result = black.format_str(result, mode=black.FileMode())
        return result

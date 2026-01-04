import pathlib
import traceback

import jinja2
import black

import jubladb_api.core.metamodel_classes as classes

def dict_items(di: dict):
    return di.items()

def snake_case_to_pascal_case(sc: str) -> str:
    words = sc.split("_")
    return "".join(w.title() for w in words)

def attribute_type_to_python_type(attr_type: "classes.AttributeType") -> str:
    attr_type_to_py_class = {
        classes.AttributeType.INTEGER: "int",
        classes.AttributeType.BOOLEAN: "bool",
        classes.AttributeType.STRING: "str",
        classes.AttributeType.FLOAT: "float",
        classes.AttributeType.DATE: "datetime.date",
        classes.AttributeType.TIME: "datetime.time",
        classes.AttributeType.DATETIME: "datetime.datetime",
    }
    return attr_type_to_py_class[attr_type]

def entity_has_sortable_attributes(entity: "classes.Entity") -> bool:
    return any(attr.sortable for attr in entity.attributes)

class TemplatedGenerator(object):
    def __init__(self):
        template_dir =  pathlib.Path(__file__).parent / "templates"
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir),
            autoescape=jinja2.select_autoescape(),
        )
        self.env.filters["snake_case_to_pascal_case"] = snake_case_to_pascal_case
        self.env.filters["attribute_type_to_python_type"] = attribute_type_to_python_type
        self.env.filters["entity_has_sortable_attributes"] = entity_has_sortable_attributes
        self.env.filters["repr"] = repr
        self.env.filters["dict_items"] = dict_items

        self.templates: dict[str, jinja2.Template] = {}

    def renderer(self, template_name: str) -> "TemplateRenderer":
        if template_name not in self.templates:
            self.templates[template_name] = self.env.get_template(template_name)
        return TemplateRenderer(self.templates[template_name])

class TemplateRenderer(object):
    def __init__(self, template: jinja2.Template):
        self.template = template

    def render(self, context: dict, reformat=True) -> str:
        result = self.template.render(**context)
        if reformat:
            try:
                result = black.format_str(result, mode=black.FileMode())
            except Exception as e:
                print("ERROR: Failed to reformat template output: ")
                traceback.print_exc()
        return result
import pathlib

import jubladb_api.metamodel
import templates

def generate_client(entities: list[jubladb_api.metamodel.Entity]):
    code_dir = pathlib.Path(__file__).parent / "../jubladb_api/client"
    generator = templates.TemplatedGenerator("client.py.jinja2")
    code = generator.render({"entities": entities})
    with open(code_dir / "client.py", "w") as f:
        f.write(code)
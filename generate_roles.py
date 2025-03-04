import requests

CODE_START = """
import dataclasses

@dataclasses.dataclass
class RoleType(object):
    id: str
    name: str
    rights: list[str]
    requires_2fa: bool
    group_type: "GroupType"
    
    def __hash__(self):
        return hash(id)
    
    def __eq__(self, other):
        return isinstance(other, RoleType) and self.id == other.id
    

@dataclasses.dataclass
class GroupType(object):
    id: str
    name: str
    role_types: list[RoleType]
    
    def __hash__(self):
        return hash(id)
        
    def __eq__(self, other):
        return isinstance(other, GroupType) and self.id == other.id
    
"""

README_MD_URL = "https://raw.githubusercontent.com/hitobito/hitobito_jubla/refs/heads/master/README.md"
ROLES_START = "<!-- roles:start -->"
ROLES_END = "<!-- roles:end -->"


def generate_roles():
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
    with open("./jubladb_api/const/groups_roles.py", "w") as f:
        f.write(CODE_START)
        group_var_names: dict[str, str] = {}
        role_var_names: dict[str, str] = {}
        role_var_names_by_group_var_name: dict[str, list[str]] = {}
        for group_id, full_name in groups.items():
            var_name = group_id.upper().replace("::", "_")
            group_var_names[group_id] = var_name
            f.write(f"{var_name} = GroupType(\"{group_id}\", \"{full_name}\", [])\n")
            role_var_names_by_group_var_name[var_name] = []
        f.write("\n")

        for role_id, name, rights, requires_2fa in roles:
            var_name = role_id.upper().replace("::", "_").replace("GROUP", "ROLE", 1)
            group_id = role_id.rsplit("::", 1)[0]
            group_var_n = group_var_names[group_id]
            rights_str = ", ".join(f"\"{r}\"" for r in rights)
            f.write(
                f"{var_name} = RoleType(\"{role_id}\", \"{name}\", [{rights_str}], {requires_2fa}, {group_var_n})\n")
            role_var_names_by_group_var_name[group_var_n].append(var_name)
            role_var_names[role_id] = var_name
        f.write("\n")

        for group_var_n, group_role_var_names in role_var_names_by_group_var_name.items():
            roles_str = ", ".join(group_role_var_names)
            f.write(f"{group_var_n}.role_types = [{roles_str}]\n")
        f.write("\n")

        f.write("ALL_GROUPS = {\n")
        for group_id, group_var_n in group_var_names.items():
            f.write(f"    \"{group_id}\": {group_var_n},\n")
        f.write("}\n")
        f.write("\n")

        f.write("ALL_ROLES = {\n")
        for role_id, role_var_name in role_var_names.items():
            f.write(f"    \"{role_id}\": {role_var_name},\n")
        f.write("}\n")


if __name__ == '__main__':
    generate_roles()

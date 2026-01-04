import dataclasses
import enum

class _EnumReprHelper(object):
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"

class Operation(_EnumReprHelper, enum.Enum):
    GetList = "GetList"
    GetSingle = "GetSingle"
    CreateSingle = "CreateSingle"
    UpdateSingle = "UpdateSingle"
    DeleteSingle = "DeleteSingle"



class AttributeType(_EnumReprHelper, enum.Enum):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    DATE = "date"
    TIME = "time"
    DATETIME = "datetime"
    BOOLEAN = "boolean"

@dataclasses.dataclass
class Attribute:
    name: str
    type_: AttributeType
    sortable: bool = False
    filter_types: set[str] = dataclasses.field(default_factory=set)

@dataclasses.dataclass
class Entity:
    url: str
    name_singular: str
    name_plural: str
    allowed_operations: set[Operation] = dataclasses.field(default_factory=set)
    attributes: list[Attribute] = dataclasses.field(default_factory=list)
    includeable: list[str] = dataclasses.field(default_factory=list)

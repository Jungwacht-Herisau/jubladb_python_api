import typing

import jubladb_api.core.metamodel_classes
import abc

class BaseEntity(abc.ABC):
    def __init__(self, id_: int):
        self._id = id_

    @property
    def id(self) -> int:
        return self._id

    @property
    @abc.abstractmethod
    def meta(self) -> jubladb_api.core.metamodel_classes.Entity:
        pass

    @classmethod
    @abc.abstractmethod
    def from_json(cls, json_dict: dict):
        pass

    @classmethod
    def _access_json_single_relation_id(cls, json_data: dict, relation_name: str, related_type_name_plural: str) -> int:
        json_relation_data = json_data["relationships"][relation_name]["data"]
        if json_relation_data["type"] != related_type_name_plural:
            raise ValueError(f"Expected relation {related_type_name_plural}, got {json_relation_data['type']}")
        return int(json_relation_data["id"])

    @classmethod
    def _access_json_many_relation_ids(cls, json_data: dict, relation_name: str, related_type_name_plural: str) -> typing.Iterable[int]:
        for json_relation_data in json_data["relationships"][relation_name]["data"]:
            if json_relation_data["type"] != related_type_name_plural:
                raise ValueError(f"Expected relation {related_type_name_plural}, got {json_relation_data['type']}")
            yield int(json_relation_data["id"])


class BaseEntityKey(abc.ABC):
    def __init__(self, id_: int):
        self._id = id_

    @property
    @abc.abstractmethod
    def type(self) -> str:
        pass

    @property
    def id(self) -> int:
        return self._id

    def __hash__(self):
        return hash(self.type) + 31*hash(self.id)

    def __eq__(self, other):
        return isinstance(other, BaseEntityKey) and self.type == other.type and self.id == other.id

    def __str__(self):
        return f"{self.type}:{self.id}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"
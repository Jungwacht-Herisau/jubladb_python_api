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
    def key(self) -> "BaseEntityKey":
        pass

    @property
    @abc.abstractmethod
    def meta(self) -> jubladb_api.core.metamodel_classes.Entity:
        pass

    @abc.abstractmethod
    def is_relation_loaded(self, relation_name: str) -> bool:
        pass

    @classmethod
    @abc.abstractmethod
    def from_json(cls, json_dict: dict):
        pass

    @classmethod
    def _access_json_single_relation_id(cls, json_data: dict, relation_name: str, related_type_name_plural: str) -> int | None:
        json_relationship = json_data["relationships"][relation_name]
        if "data" not in json_relationship:
            json_meta = json_relationship.get("meta", {})
            if not json_meta.get("included", False):
                return None
            else:
                raise ValueError(f"Expected relation {related_type_name_plural} to either have data or included: false")
        json_relation_data = json_relationship["data"]
        if json_relation_data["type"] != related_type_name_plural:
            raise ValueError(f"Expected relation {related_type_name_plural}, got {json_relation_data['type']}")
        return int(json_relation_data["id"])

    @classmethod
    def _create_single_relation_key(cls, json_data: dict, relation_name: str, related_type_name_plural: str, key_class):
        relation_id = cls._access_json_single_relation_id(json_data, relation_name, related_type_name_plural)
        return key_class(relation_id) if relation_id is not None else None

    @classmethod
    def _access_json_many_relation_ids(cls, json_data: dict, relation_name: str, related_type_name_plural: str) -> list[int] | None:
        json_relationship = json_data["relationships"][relation_name]
        if "data" not in json_relationship:
            json_meta = json_relationship.get("meta", {})
            if not json_meta.get("included", False):
                return None
            else:
                raise ValueError(f"Expected relation {related_type_name_plural} to either have data or included: false")
        res: list[int] = []
        for json_relation_data in json_relationship["data"]:
            if json_relation_data["type"] != related_type_name_plural:
                raise ValueError(f"Expected relation {related_type_name_plural}, got {json_relation_data['type']}")
            res.append(int(json_relation_data["id"]))
        return res

    @classmethod
    def _create_many_relation_keys(cls, json_data: dict, relation_name: str, related_type_name_plural: str, key_class):
        relation_ids = cls._access_json_many_relation_ids(json_data, relation_name, related_type_name_plural)
        return [key_class(rid) for rid in relation_ids] if relation_ids is not None else None

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.id})"


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
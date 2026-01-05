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
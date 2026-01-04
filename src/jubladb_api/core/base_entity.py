import jubladb_api.core.metamodel_classes
import abc

class EntityBase(abc.ABC):
    def __init__(self, id_: int):
        self._id = id_

    @property
    def id(self) -> int:
        return self._id

    @property
    @abc.abstractmethod
    def meta(self) -> jubladb_api.core.metamodel_classes.Entity:
        pass
from abc import ABC, abstractmethod

from properties.seedwork.domain.entities import Entity


class Repository(ABC):

    @abstractmethod
    def update(self, entity: Entity): ...


class Mapper(ABC):

    @abstractmethod
    def get_type(self) -> type: ...

    @abstractmethod
    def entity_2_dto(self, entity: Entity) -> any: ...

    @abstractmethod
    def dto_2_entity(self, dto: any) -> Entity: ...

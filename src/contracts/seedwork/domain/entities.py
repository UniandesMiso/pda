from uuid import UUID, uuid4
from datetime import datetime
from dataclasses import dataclass, field

from contracts.seedwork.domain.events import DomainEvent
from contracts.seedwork.domain.value_objects import Amount


@dataclass
class Entity:
    id: UUID = field(hash=True)
    _id: UUID = field(init=False, repr=False, hash=True)
    created_at: datetime = field(default=datetime.now())
    updated_at: datetime = field(default=datetime.now())

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: UUID) -> None:
        self._id = uuid4()


@dataclass
class Root(Entity):
    events: list[DomainEvent] = field(default_factory=list)

    def add_event(self, event):
        self.events.append(event)

    def clear_events(self):
        self.events = list()


@dataclass
class Contract(Root):
    amount: Amount = field(default_factory=Amount)

from uuid import UUID, uuid4
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class DomainEvent:
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

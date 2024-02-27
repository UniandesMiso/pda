from dataclasses import dataclass, field

from properties.seedwork.application.dto import DTO


@dataclass(frozen=True)
class GroundDTO(DTO):
    id: str = field(default_factory=str)
    status: str = field(default_factory=str)
    address: str = field(default_factory=str)

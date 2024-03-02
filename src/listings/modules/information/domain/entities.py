from datetime import datetime
from dataclasses import dataclass, field

from listings.seedwork.domain.entities import Contract
from listings.seedwork.domain.mixins import ValidateRules
from listings.modules.information.domain.events import PropertyProcessed


@dataclass
class Listing(Contract, ValidateRules):
    executed_at: datetime = field(default=datetime.now())

    def process_listing(self):
        for property in self.properties:
            event = PropertyProcessed(
                property_id=property.id,
                width=property.width,
                length=property.length,
                executed_at=self.executed_at,
            )
            self.add_event(event)

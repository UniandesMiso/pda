from dataclasses import dataclass

from properties.seedwork.domain.entities import Property
from properties.modules.grounds.domain.events import AmountUpdated


@dataclass
class Ground(Property):

    def update_amount(self):
        event = AmountUpdated(
            ground_id=self.id,
            price=self.amount.price,
            currency=self.amount.currency,
        )
        self.add_event(event)

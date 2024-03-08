from dataclasses import dataclass

from properties.seedwork.application.commands import Command


class SaleCommand(Command): ...


@dataclass
class RegisterSale(SaleCommand):
    property_id: str
    price: float
    currency: str
    executed_at: str


@dataclass
class DeleteSale(SaleCommand):
    sale_id: str

from properties.seedwork.application.handlers import Handler
from properties.seedwork.application.commands import execute_command
from properties.modules.grounds.application.commands.update_ground_price import UpdateGroundPrice


class GroundsHandler(Handler):

    @staticmethod
    def handle_sale_registered(event):
        command = UpdateGroundPrice(
            id=event.data.property_id,
            price=event.data.price,
            currency=event.data.currency
        )
        execute_command(command)

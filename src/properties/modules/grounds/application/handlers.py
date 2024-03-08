from properties.seedwork.application.handlers import Handler
from properties.seedwork.application.commands import execute_command
from properties.modules.grounds.application.commands.update_ground_amount import UpdateGroundAmount
from properties.modules.grounds.application.commands.update_ground_dimension import UpdateGroundDimension


class GroundsHandler(Handler):

    @staticmethod
    def handle_sale_registered(event):
        command = UpdateGroundAmount(
            id=event.data.property_id,
            price=event.data.price,
            currency=event.data.currency,
        )
        execute_command(command)

    @staticmethod
    def handle_property_processed(event):
        command = UpdateGroundDimension(
            id=event.data.property_id,
            width=event.data.width,
            length=event.data.length,
        )
        execute_command(command)

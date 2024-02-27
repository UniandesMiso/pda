from properties.seedwork.application.handlers import Handler
from properties.seedwork.application.commands import execute_command
from properties.modules.grounds.application.commands.update_ground_status import UpdateGroundStatus


class GroundsHandler(Handler):

    @staticmethod
    def handle_sale_registered(event):
        command = UpdateGroundStatus(id="1234")
        result = execute_command(command)
        print("command executed:", result.data)

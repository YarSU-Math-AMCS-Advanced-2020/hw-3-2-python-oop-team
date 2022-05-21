from request import Request


class AbstractCommand:
    def __init__(self, request: Request):
        self.command = request.get_command()
        self.client_id = request.get_client_id()
        self.params_dict = request.get_params_dict()

    def execute(self):
        pass

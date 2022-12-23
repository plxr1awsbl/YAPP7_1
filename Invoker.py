class Invoker:
    def __init__(self, command=None):
        self.command = command

    def set_command(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()

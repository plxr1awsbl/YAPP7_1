import abc


class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass


class SortAscendingCommand(Command):

    def __init__(self, this_file):
        self.this_file = this_file

    def execute(self):
        self.this_file.sort_ascending()
        self.this_file.printStrings()


class SortDescendingCommand(Command):

    def __init__(self, this_file):
        self.this_file = this_file

    def execute(self):
        self.this_file.sort_descending()
        self.this_file.printStrings()


class SortRandomCommand(Command):

    def __init__(self, this_file):
        self.this_file = this_file

    def execute(self):
        self.this_file.sort_random()
        self.this_file.printStrings()


class SortLenAscendingCommand(Command):

    def __init__(self, this_file):
        self.this_file = this_file

    def execute(self):
        self.this_file.sort_len_ascending()
        self.this_file.printStrings()


class SortLenDescendingCommand(Command):

    def __init__(self, this_file):
        self.this_file = this_file

    def execute(self):
        self.this_file.sort_len_descending()
        self.this_file.printStrings()


class SaveCommand(Command):

    def __init__(self, this_file):
        self.this_file = this_file

    def execute(self):
        self.this_file.save_file()
        print(f"Now your new file is located by path: {self.this_file.new_path}")


class CloseCommand(Command):
    def __int__(self, file):
        self.this_file = file

    def execute(self):
        self.this_file.close_file()
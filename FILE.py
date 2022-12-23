from random import shuffle


class FILE(object):

    def __init__(self, open_path, new_path):
        try:
            self.old_file = open(open_path)
            self.strings = [line.rstrip() for line in self.old_file.readlines()]
            self.old_file.close()
            self.new_path = new_path

        except:
            print("Impossible to open existing file, mb try another path")

        try:
            self.file = open(new_path, 'w')

        except:
            print("Impossible to create new file, mb try another path or smth idk...")

    def printStrings(self):
        print(self.strings, "\n")

    def sort_ascending(self):
        self.strings.sort()

    def sort_descending(self):
        self.strings.sort(reverse=True)

    def sort_random(self):
        shuffle(self.strings)

    def sort_len_ascending(self):
        count = len(self.strings)

        for i in range(count-1):
            for j in range(count - i - 1):
                if len(self.strings[j]) > len(self.strings[j+1]):
                    self.strings[j], self.strings[j+1] = self.strings[j+1], self.strings[j]

    def sort_len_descending(self):
        count = len(self.strings)

        for i in range(count - 1):
            for j in range(count - i - 1):
                if len(self.strings[j]) < len(self.strings[j + 1]):
                    self.strings[j], self.strings[j + 1] = self.strings[j + 1], self.strings[j]

    def save_file(self):
        for line in self.strings:
            self.file.write(line + '\n')

        self.file.close()

    def close_file(self):
        self.file.close()
from FILE import FILE
from Invoker import Invoker
import Command as cm


old_path = input("Enter the path to existing file: ")
new_path = input("Enter the path you want to save new file: ")

file = FILE(old_path, new_path)
print("\nNow you have:\n")
file.printStrings()


print("Enter the operation number you want:\n"
      "1) Sort lines by ascending\n"
      "2) Sort lines by descending\n"
      "3) Sort lines randomly\n"
      "4) Sort lines by ascending of their len\n"
      "5) Sort lines by descending of their len\n")
op_num = input()


if op_num == '1':
      command = cm.SortAscendingCommand(file)

elif op_num == '2':
      command = cm.SortDescendingCommand(file)

elif op_num == '3':
      command = cm.SortRandomCommand(file)

elif op_num == '4':
      command = cm.SortLenAscendingCommand(file)

elif op_num == '5':
      command = cm.SortLenDescendingCommand(file)
else:
      print("Command number is incorrect, I will just do what I want.")
      command = cm.SortRandomCommand(file)

invoker = Invoker(command)
invoker.invoke()
invoker.set_command(cm.SaveCommand(file))
invoker.invoke()
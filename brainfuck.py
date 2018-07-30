import sys

list_ = [0] * 1000

while 1:
    command = input()
    if command == "reset":
        list_ = [0] * 1000
    if command == "exit":
        break

    command_list = list(command)
    pointer = 0
    for i in command_list:
        if i == ">" and pointer < 1000:
            pointer = pointer + 1
        if i == "<" and pointer > 0:
            pointer = pointer - 1
        if i == "+":
            list_[pointer] = list_[pointer] + 1
        if i == "-":
            list_[pointer] = list_[pointer] - 1
        if i == ".":
            sys.stdout.write(chr(list_[pointer]))
        if i == ",":
            list_[pointer] = ord(input("> "))
    print()

import sys

length = 1000
list_ = [0] * length

while 1:
    command = input()
    if command == "reset":
        list_ = [0] * length
        pointer = 0
    if command == "exit":
        break

    command_list = list(command)
    pointer = 0
    i = 0
    while i < len(command_list):
        if command_list[i] == ">" and pointer < 1000:
            pointer = pointer + 1
        if command_list[i] == "<" and pointer > 0:
            pointer = pointer - 1
        if command_list[i] == "+":
            list_[pointer] = list_[pointer] + 1
        if command_list[i] == "-":
            list_[pointer] = list_[pointer] - 1
        if command_list[i] == ".":
            sys.stdout.write(chr(list_[pointer]))
        if command_list[i] == ",":
            list_[pointer] = ord(input("> "))
        if command_list[i] == "[" and list_[pointer] == 0:
            j = i + 1
            while j < length:
                if command_list[j] == "]":
                    i = j
                    k = 1
                    break
                j = j + 1
        if command_list[i] == "]" and k == 0:
            j = i - 1
            while j >= 0:
                if command_list[j] == "[":
                    i = j - 1
                    break
                j = j - 1
        i = i + 1
        k = 0
    print()

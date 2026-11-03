import sys


def main():
    while True:
        command = input("$ ")
        if command == "exit":
            break
        command_list = command.split(" ")
        if command_list[0] == "echo":
            print(" ".join(command_list[1:]))
        else:
            print(f"{command}: command not found")
    


if __name__ == "__main__":
    main()

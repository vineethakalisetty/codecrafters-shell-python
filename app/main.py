import sys
import os


def main():
    while True:
        command = input("$ ")
        if command == "exit":
            break
        command_list = command.split(" ")
        if command_list[0] == "echo":
            print(" ".join(command_list[1:]))
        elif command_list[0] == "type":
            if command[5:] in ["echo", "exit", "type"]:
                print(f"{command[5:]} is a shell builtin")
            else:
                path = os.environ.get("PATH", "")
                executable = False
                for directory in path.split(os.pathsep):
                    candidate = os.path.join(directory, command[5:])
                    if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
                        executable = True
                        print(command[5:], " is ", candidate)
                        break
                if executable == False:
                    print(f"{command[5:]}: not found")
        else:
            print(f"{command}: command not found")
    


if __name__ == "__main__":
    main()

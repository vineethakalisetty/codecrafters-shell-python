from re import sub
import sys
import os
import subprocess

def find_executable(name):
    path = os.environ.get("PATH", "")
    for directory in path.split(os.pathsep):
        file_path = os.path.join(directory, name)
        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            return file_path
    return None

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
                executable = find_executable(command[5:])
                if executable:
                    print(f"{command[5:]} is {executable} ")
                else:
                    print(f"{command[5:]}: not found")

                # path = os.environ.get("PATH", "")
                # executable = False
                # for directory in path.split(os.pathsep):
                #     candidate = os.path.join(directory, command[5:])
                #     if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
                #         executable = True
                #         print(command[5:], "is", candidate)
                #         break
                # if executable == False:
                #     print(f"{command[5:]}: not found")
        else:
            executable = find_executable(command_list[0])
            if executable:
                output = subprocess.run(command_list, capture_output=True, text=True)
                print(output.stdout, end = "")
            else:
                print(f"{command}: command not found")
            # path = os.environ.get("PATH", "")
            # executable = False
            # for directory in path.split(os.pathsep):
            #     candidate = os.path.join(directory, command_list[0])
            #     if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            #         executable = True
            #         break
            # if executable == True:
            #     output = subprocess.run(command_list, capture_output=True, text=True)
            #     print(output.stdout, end = "")
            
            # else:
            #     print(f"{command}: command not found")
    


if __name__ == "__main__":
    main()

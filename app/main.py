import sys


def main():
    while True:
        command = input("$ ")
        if command == "exit":
            break
        print(f"{command}: command not found")
    


if __name__ == "__main__":
    main()

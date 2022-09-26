import os
import sys

class Program:
    def __init__(self, program_name, version):
        self.program_name = program_name
        self.version = version

    def line_breaker(self):
        print("=====================================\n")

    # prints the program header
    def program_header(self):
        print(f"{self.program_name} - {self.version}")
        self.line_breaker()

    # ask in console for use input
    def user_input(self):
        user_input = input("Your choice: ")
        return user_input

    def print_menu_options(self, dictionary):
        for key in dictionary:
            print(f"{key}: {dictionary.get(key)}")
        print("\n")

    def clear(self):
        # Windows
        if os.name == "nt":
            _ = os.system('cls')
        
        # Unix like, linux & macOS
        else:
            _ = os.system('clear')
    
    def exit(self):
        self.clear()
        sys.exit()
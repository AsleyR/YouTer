from winds.program_class import Program

class OtherSaveLocationWindow(Program):
    def __init__(self):
        self.window_message = "Make sure to enter a valid location.\n"

    def init_window(self):
        while True:
            self.clear()

            print("Other Save Location")
            self.line_breaker()
            print(self.window_message)

            user_input = input("Save location: ")

            if user_input != "":
                return user_input

            else:
                print("\nThe save location cannot be a empty space!\n")
                print("Press any key to try again...")

                input('') # empty input to hold loop

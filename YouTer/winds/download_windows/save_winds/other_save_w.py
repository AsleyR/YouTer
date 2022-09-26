from YouTer.winds.class_templates.program_class import Program
from YouTer.winds.download_windows.link_w import LinkWindow

class OtherSaveLocationWindow(Program):
    def __init__(self, command):
        self.window_message = "Make sure to enter a valid location.\n"
        self.command = command

    def init_window(self):
        while True:
            self.clear()

            print("Other Save Location")
            self.line_breaker()
            print(self.window_message)

            user_input = input("Save location: ")

            if user_input != "":
                file_path = user_input + "/%(title)s.%(ext)s"

                return file_path

            else:
                print("\nThe save location cannot be a empty space!\n")
                print("Press any key to try again...")

                input('') # empty input to hold loop

from os import link
from winds.class_templates.program_class import Program
from winds.download_windows.save_winds.other_save_w import OtherSaveLocationWindow
from winds.download_windows.link_w import LinkWindow

class SaveLocationWindow(Program):
    def __init__(self, command):
        self.command = command
        self.menu_options = {
            1: "Save on Desktop (Default)",
            2: "Enter custom save location",
            3: "Return to previous window"
        }

    def init_window(self):
        DEFAULT_FILE_PATH = "~/Desktop/%(title)s.%(ext)s"
        while True:
            self.clear()

            # Print Save location header
            print("Save location")
            self.line_breaker()

            self.print_menu_options(self.menu_options)

            user_input = self.user_input()

            if user_input == "1":
                link_w = LinkWindow(DEFAULT_FILE_PATH, self.command)
                link_w.init_window()
            
            elif user_input == "2":
                other_save_w = OtherSaveLocationWindow(self.command)
                custom_file_path = other_save_w.init_window()

                link_w = LinkWindow(custom_file_path, self.command)
                link_w.init_window()

            elif user_input == "3":
                break

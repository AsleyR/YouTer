from winds.program_class import Program
from winds.download_windows.other_save_w import OtherSaveLocationWindow
from winds.download_windows.link_w import LinkWindow

class SaveLocationWindow(Program):
    def __init__(self):
        self.menu_options = {
            1: "Save on Desktop (Default)",
            2: "Enter custom save location",
            3: "Return to previous window"
        }

    def init_window(self):
        while True:
            self.clear()

            # Print Save location header
            print("Save location")
            self.line_breaker()

            self.print_menu_options(self.menu_options)

            user_input = self.user_input()

            if user_input == "1":
                link_w = LinkWindow()
                link_w.init_window()
            
            elif user_input == "2":
                other_save_w = OtherSaveLocationWindow()
                other_save_w.init_window()

            elif user_input == "3":
                break

from winds.class_templates.program_class import Program

class OptionsWindow(Program):
    def __init__(self):
        self.options_menu = {
            1: "Clear console per action",
            2: "Return to main menu"
        }
    
    # Get all options from options_menu dict
    def print_options(self):
        menu = self.options_menu
        for key in menu:
            print(f"{key}: {menu.get(key)}")
        print('\n')

    def options_window(self):
        print("Options")
        self.line_breaker()
        self.print_options()
        self.user_input()
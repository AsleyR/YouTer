from YouTer.winds.class_templates.program_class import Program

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

    def init_window(self):
        while True:
            self.clear() # Clear console

            print("Options (Not working at the moment)")
            self.line_breaker()
            self.print_options()

            # Ask for User Input
            user_input = self.user_input()

            # if 1, change settings
            if (user_input == '1'):
                break
            # if 2, return to main menu
            elif (user_input == '2'):
                break
            # in case of another input
            else:
                pass
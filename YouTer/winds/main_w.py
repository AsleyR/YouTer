from .class_templates.program_class import Program

class MainWindow(Program):
    def __init__(self, program_name, version):
        super().__init__(program_name, version)
        self.menu_options = {
            1: "Download Video",
            2: "Download Audio",
            3: "Custom youtube-dl Command",
            4: "About",
            5: "Options",
            6: "Exit"
        }

    def init_program(self):
        self.clear()
        self.program_header()
        
        self.print_menu_options(self.menu_options)
        user_input = self.user_input()

        return user_input
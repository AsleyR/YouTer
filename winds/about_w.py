import os
from winds.class_templates.program_class import Program

class AboutWindow(Program):
    def __init__(self, program_name, author_name, version):
        self.about_file_path = os.path.join(os.getcwd())
        self.author_name = author_name
        super().__init__(program_name, version)

    # Checks to see if the program is being run as package or script
    # in order to properly locate the .txt file about.txt

    def check_file_path(self):
        # check if run as a package
        if os.path.exists(os.path.join(os.getcwd(), 'ytdl-tgui', 'texts', 'about.txt')):
            self.about_file_path = os.path.join(os.getcwd(), 'ytdl-tgui', 'texts', 'about.txt')

        # check if run as a script
        elif os.path.exists(os.path.join(os.getcwd(), 'texts', 'about.txt')):
            self.about_file_path = os.path.join(os.getcwd(), 'texts', 'about.txt')

        else:
            print('Error locating file')
            input('\nPress any key to restart the process...')

    def read_about_file(self):
        about_text = []
        with open(self.about_file_path, 'r') as f:
            for line in f:
                about_text.append(line)
            f.close() # Remember to always close the opened files...
        return about_text

    # Init window
    def init_window(self):
        self.check_file_path()

        self.clear()

        # About section header
        print("About Program")
        self.line_breaker()
        print(f"{self.program_name} - V{self.version}\n")

        # Print contents of about.txt
        file_lines = self.read_about_file()
        for line in file_lines:
            print(line)
        
        print(f'\nMade by {self.author_name} (2022).\n')
        self.line_breaker()

        input('Press any key to return to main menu...')
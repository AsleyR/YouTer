from winds.class_templates.program_class import Program

class AboutWindow(Program):
    def __init__(self, author_name, version):
        self.author_name = author_name
        self.version = version

    def read_about_file(self):
        about_text = []
        with open('./texts/about.txt', 'r') as f:
            for line in f:
                about_text.append(line)
            f.close()
        return about_text

    def print_about(self):
        self.clear()

        # About section header
        print("About Program")
        self.line_breaker()

        # Print contents of about.txt
        file_lines = self.read_about_file()
        for line in file_lines:
            print(line)
        
        print(f'\nMade by {self.author_name} (2022).')
        print(self.version)
        self.line_breaker()

        input('\nPress any key to return to main menu...')

# example = AboutWindow()
# example.print_about()
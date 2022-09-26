import os
from YouTer.winds.class_templates.program_class import Program

class YoutubeDlWindow(Program):
    def __init__(self, command):
        self.command = command

    def init_window(self):
        self.clear()

        print("Download with youtube-dl")
        self.line_breaker()

        final_command = f"youtube-dl {self.command}"

        print(f"Final command: \n{final_command}\n")
        print("Now running youtube-dl...\n")

        os.system(final_command)

        print('\n')
        input("Press any key to restart the program...")
        return


from .class_templates.program_class import Program
from .download_windows.youtubedl_w import YoutubeDlWindow

class CustomYoutubeDlCommandWindow(Program):
    def __init__(self):
        pass

    def init_window(self):
        while True:
            self.clear()
            print("Custom Youtube-dl Command")
            self.line_breaker()
            
            print("Note: Enter your custom command after 'youtube-dl'\n")
            user_input = input("Command: youtube-dl ")

            if user_input != "":
                youtubedl_w = YoutubeDlWindow(user_input)
                youtubedl_w.init_window()
                break
            else:
                print("\nThe command can't be an empty string o.O\n")
                input('Press any key to try again... ')



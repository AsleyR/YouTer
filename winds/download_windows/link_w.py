from winds.class_templates.program_class import Program
from winds.download_windows.youtubedl_w import YoutubeDlWindow

class LinkWindow(Program):
    def __init__(self, file_path, command):
        self.file_path = file_path
        self.command = command

    def init_window(self):
        self.clear()
        print("Enter Link")
        self.line_breaker()

        user_input = input("Enter video link (no spaces): ")

        final_command = f"{self.command} -o '{self.file_path}' {user_input}"

        youtubedl_w = YoutubeDlWindow(final_command)
        youtubedl_w.init_window()
        return user_input
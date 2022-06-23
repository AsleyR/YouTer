from winds.program_class import Program

class SpecificQualityOptionWindow(Program):
    def __init__(self):
        self.menu_message = "Please note that the final file may not end up in .mp4 format\n"
        self.menu_options = {
            1: "144p",
            2: "240p",
            3: "360p",
            4: "480p",
            5: "720p",
            6: "1080p",
            7: "1440p",
            8: "2160p"
        }

    def init_window(self):
        while True:
            self.clear()

            print("Select Specific Quality")
            self.line_breaker()

            print(self.menu_message)

            self.print_menu_options(self.menu_options)

            user_input = self.user_input()

            # Temporal solution
            if user_input == "":
                pass
            else:
             return user_input
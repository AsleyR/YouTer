from YouTer.winds.class_templates.program_class import Program

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

    def get_quality_value(self, input):
        quality = []
        menu = self.menu_options
        for key in menu:
            if input == str(key):
                # input(' ')
                quality.append(self.menu_options.get(key))

        # Check if list has any value, cause if it has, then input was found in self.menu_options values.
        if len(quality) != 0:
            output_command = f"-f 'bestvideo[height={quality[0]}] +bestaudio[ext=m4a]/best[ext=mp4]/best'"
            return output_command
        else:
            return "error"



    def init_window(self):
        while True:
            first_part_command = "" # Reset value
            self.clear()

            print("Select Specific Quality")
            self.line_breaker()

            print(self.menu_message)

            self.print_menu_options(self.menu_options)

            user_input = self.user_input()

            # Purge user_inputs that are not valid
            if user_input == "":
                pass
            else:
                # Find out if user input is found in self.menu_options
                first_part_command = self.get_quality_value(user_input)

                # In case user_input is not found
                if first_part_command == "error":
                    pass # Continue with loop to restart process

                # Value found, returning youtube-dl command with specific quality
                else:
                    specific_quality_command = f"{first_part_command} --merge-output-format mp4"
                    return specific_quality_command
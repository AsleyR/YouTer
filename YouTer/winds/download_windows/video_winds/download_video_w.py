from numpy import save
from winds.class_templates.program_class import Program
from winds.download_windows.save_winds.save_w import SaveLocationWindow
from winds.download_windows.video_winds.specific_quality_w import SpecificQualityOptionWindow

class VideoDownloadWindow(Program):
    def __init__(self):
        self.window_options = {
            1: "Best posible quality (Default)",
            2: "Select a specific quality",
            3: "Return to main menu"
        }

    def init_window(self):
        BEST_QUALITY_COMMAND = "-f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'"

        # Init window loop
        while True:
            self.clear()
            print("Download Video")
            self.line_breaker()

            self.print_menu_options(self.window_options)

            user_input = self.user_input()

            if user_input == "1":
                save_w = SaveLocationWindow(BEST_QUALITY_COMMAND)
                save_w.init_window()
                break
            
            elif user_input == "2":
                s_quality_w = SpecificQualityOptionWindow()
                special_quality = s_quality_w.init_window()

                save_w = SaveLocationWindow(special_quality)
                save_w.init_window()
                break
            
            elif user_input == "3":
                break


    
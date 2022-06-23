from numpy import save
from winds.program_class import Program
from winds.download_windows.save_w import SaveLocationWindow
from winds.download_windows.specific_quality_w import SpecificQualityOptionWindow

class VideoDownloadWindow(Program):
    def __init__(self):
        self.window_options = {
            1: "Best posible quality (Default)",
            2: "Select a specific quality",
            3: "Return to main menu"
        }

    def init_window(self):
        while True:
            self.clear()
            print("Download Video")
            self.line_breaker()

            self.print_menu_options(self.window_options)

            user_input = self.user_input()

            if user_input == "1":
                save_w = SaveLocationWindow()
                save_w.init_window()
            
            elif user_input == "2":
                s_quality_w = SpecificQualityOptionWindow()
                s_quality_w.init_window()
            
            elif user_input == "3":
                break


    
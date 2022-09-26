from .winds.main_w import MainWindow
from .winds.about_w import AboutWindow
from .winds.custom_command import CustomYoutubeDlCommandWindow
from .winds.download_windows.video_winds.download_video_w import VideoDownloadWindow
from .winds.download_windows.save_winds.save_w import SaveLocationWindow
from .winds.options_w import OptionsWindow

def main_program():
    PROGRAM_NAME = "YouTer"
    CURRENT_VERSION = "1.0.1"
    AUDIO_YOUTUBEDL_COMMAND = "-x --audio-format mp3"

    try:
        while True:

            # Init MainWindow
            main_program = MainWindow(PROGRAM_NAME, CURRENT_VERSION)
            user_input = main_program.init_program()
            print(f"You chose: {user_input}")

            # Save Window
            if user_input == '1':
                download_video_w = VideoDownloadWindow()
                download_video_w.init_window()
            
            elif user_input == "2":
                save_window = SaveLocationWindow(AUDIO_YOUTUBEDL_COMMAND)
                save_window.init_window()

            elif user_input == "3":
                custom_command_w = CustomYoutubeDlCommandWindow()
                custom_command_w.init_window()

            elif user_input == '4':
                about_w = AboutWindow(PROGRAM_NAME, "Asley R.", CURRENT_VERSION)
                about_w.init_window()
            
            elif user_input == '5':
                options_w = OptionsWindow()
                options_w.init_window()

            elif user_input == '6':
                # Exit program
                main_program.exit()

    except KeyboardInterrupt: # Control C keyboard interrupt
        main_program.exit()

# Init script
if __name__ == "__main__":
    main_program()


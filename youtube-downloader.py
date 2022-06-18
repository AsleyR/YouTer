import os
import sys

# =========== Global Variables ===========

# Note: This is bad practice, however, I am not sure how to not use global variables in a program like this
# I have tried to shape it into more of a more modular program that doesn't use global variables but for
# some reason I can't get it to compile all the files and directories with pyinstaller.

program_version = 'V. 1.6.3'

dl_video = 'youtube-dl -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"'
dl_audio = 'youtube-dl -x --audio-format mp3'

video_quality = False
video_ql_options = ['144', '240', '360', '480', '720', '1080', '1440', '2160']
quality_command = '-f "bestvideo'

default_address = '"~/Desktop/'
address_ext = '%(title)s.%(ext)s"'

error_answer = 'Please, choose a valid answer'

running = True

options_window = False
clr_console_action = True

# =========== END - Global Variables ===========

# =========== Functions ===========

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac or linux
    else:
        _ = os.system('clear')

def header():
    print('Youtube Downloader - ' + program_version)
    print('==============================\n')

def error_message():
    print('\n' + error_answer + '\n')
    input('')

def get_quality_input(user_input, arg_list):
    switcher = {
        1: arg_list[0],
        2: arg_list[1],
        3: arg_list[2],
        4: arg_list[3],
        5: arg_list[4],
        6: arg_list[5],
        7: arg_list[6],
        8: arg_list[7]
    }

    return switcher.get(user_input, "error") # Switch dictionary

# =========== End - Functions ===========

# =========== Main Program ===========

while True:
    clear()
    header()

    while True:
        print('1: Download Video\n2: Download Audio\n3: About\n4: Options\n5: Exit\n')

        try:
            dl_option = int(input('Your choice: '))
            if dl_option == 1:
                command = dl_video
                video_quality = True
                break
            elif dl_option == 2:
                command = dl_audio
                break
            elif dl_option == 3:
                clear()
                print("\nThis is a small program that downloads youtube videos in mp4 or mp3 formats."
                      " It uses yt-dl and ffmpeg. So, if you want more details about any errors, I encourage you to go to "
                      "their respectives websites for a more in-depth research.\n"
                      "\nHowever, if you want more information about this tool, you are invited to read the" 
                      " README file on the github page of the project.")
                print("\nMade by: Asley R. (2021).")
                print(program_version + '\n')
                
                print('==============================\n')
                input('Press any key to return to the main menu.\n')
                clear()
                header()
            elif dl_option == 4:
                options_window = True
                
                while options_window:
                    clear()
                    print('==== Options ====')
                    print('\n1: Clear console per action (' + str(clr_console_action) + ')\n2: Return main menu\n')

                    try:
                        op_selection = int(input('Your choice: '))
                        if op_selection == 1:
                            clear()

                            while True:
                                print('Change option -- Clear console per action')
                                print('Current state: ' + str(clr_console_action) + '.\n')
                                print('1: Set to True\n2: Set to False\n')
                                
                                try:
                                    clr_console_selection = int(input('Your choice: '))
                                    if clr_console_selection == 1:
                                        clr_console_action = True
                                        clear()
                                        header()
                                        break
                                    elif clr_console_selection == 2:
                                        clr_console_action = False
                                        clear()
                                        header()
                                        break
                                    else:
                                        error_message()
                                        clear()
                                except ValueError:
                                    error_message()
                                    clear()
                        elif op_selection == 2:
                            clear()
                            header()
                            break
                    except ValueError:
                        error_message()

            elif dl_option == 5:
                clear()
                sys.exit()
            else:
                error_message()
                clear()
                header()
        except ValueError:
            error_message()
            clear()
            header()
    
    while video_quality:
        print('')
        if clr_console_action == True:
            clear()

        print('==============================')
        print('\nChoose video quality\n')
        print('1: Best possible quality (Default)\n2: Select an specific quality\n')

        try:
            v_option = int(input('Your choice: '))
            if v_option == 1:
                break
            elif v_option == 2:
                while True:
                    print('')
                    if clr_console_action == True:
                        clear()
                    
                    print('==============================')
                    print('\nSelect quality\n')
                    print('Note: Make sure the source video has the selected quality available. Otherwise, it will not work.\n'
                        "Also, it's possible that the final output may not come as an mp4 file.\n")
                    print('1: 144p\n2: 240p\n3: 360p\n4: 480p\n5: 720p\n6: 1080p\n7: 1440p\n8: 2160p\n')

                    quality_option = int(input('Your choice: '))
                    
                    # Command
                    command_video_ql = get_quality_input(quality_option, video_ql_options)
                    if command_video_ql == "error":
                        error_message();
                        print(command_video_ql)
                        break
                    else:
                        quality_selection = quality_command + '[height=' + command_video_ql + ']'
                        command = 'youtube-dl ' + quality_selection + '+bestaudio[ext=m4a]/best[ext=mp4]/best"'
                        break

                break
            else:
                error_message()
        except ValueError:
            error_message()


    while True:
        print('')
        if clr_console_action == True:
            clear()

        print('==============================')
        print('\nSave location')
        print("\n1: Default save location (Desktop)\n2: Other save location\n")

        try:
            address_option = int(input('Your choice: '))

            if address_option == 1:
                address = default_address + address_ext
                break
            elif address_option == 2:
                print('')
                if clr_console_action == True:
                    clear()
                
                while True:
                    print('==============================')
                    print("\nMake sure to enter a valid location, otherwise it will NOT work.\n")
                    address_input = str(input('Sava location: '))

                    if address_input == '':
                        print('\nAddress CANNOT be empty.')
                        input('')
                        clear()
                    else:
                        address = '"' + address_input + address_ext
                        break
                break
            else:
                error_message()

        except ValueError:
            error_message()

    print('')
    if clr_console_action == True:
        clear()
    print('==============================\n')
    link = input('Enter link (no spaces): ')
    print('')

    # Add all commands into a single one
    final_command = command + ' ' + '-o ' + address + ' ' + link

    os.system(final_command)

    input('\nPress any key to restart the process.\n')

    video_quality = False
    clear()

# =========== END - Main Program ===========

# This program is so recursive like wtf, I had to make diagrams to understand the workflow. First time I do that.
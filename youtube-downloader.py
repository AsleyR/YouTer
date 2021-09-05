import os

dl_video = 'youtube-dl -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"'
dl_audio = 'youtube-dl -x --audio-format mp3'
default_address = '"~/Desktop/'
address_ext = '%(title)s.%(ext)s"'

running = True


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac or linux
    else:
        _ = os.system('clear')


while True:
    print('Youtube Downloader - V. 1.0')
    print('==============================\n')

    while True:
        print('1: Download Video\n2: Download Audio\n3: About\n')

        try:
            dl_option = int(input('Your choice: '))
            if dl_option == 1:
                command = dl_video
                break
            elif dl_option == 2:
                command = dl_audio
                break
            elif dl_option == 3:
                print("\nThis is a small program that downloads youtube videos in mp4 or mp3 formats."
                      " It uses yt-dl. So, if want more details about any errors, I encourage you to go to: "
                      "https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme.\n")
                print("\nMade by: Asley R. (2021).\n")

                input('Press any key to return to the main menu.\n')
                clear()
            else:
                print("\nPlease, choose a valid number.\n")
        except ValueError:
            print("\nPlease, choose a valid answer.\n")

    while True:
        print("\n1: Default save location (Desktop)\n2: Other save location\n")

        try:
            address_option = int(input('Your choice: '))

            if address_option == 1:
                address = default_address + address_ext
                break
            elif address_option == 2:
                print("Make sure to enter a valid location, otherwise it will NOT work.")
                address = '"' + str(input('Save location: ')) + address_ext
                break
            else:
                print("\nPlease, choose a valid number.\n")

        except ValueError:
            print('\nPlease, choose a valid answer.')

    link = input('Enter link (no spaces): ')

    os.system(command + ' ' + "-o " + address + ' ' + link)

    input('\nPress any key to restart the process.\n')

    clear()

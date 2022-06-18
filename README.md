# ytdl-downloader
A small terminal based program that downloads youtube videos in mp4 or mp3. It uses <a href="https://youtube-dl.org/" target="_blank">youtube-dl</a> and <a href="https://ffmpeg.org/" target="_blank">ffmpeg tools</a>. The .exe version of the program was compiled using <a href="https://pyinstaller.org/en/stable/" target="_blank">PyInstaller</a>.

For more information about any errors you may encounter when attemting to download, I encourage you go look up yt-dl documentation at: https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme.

<br>

## How to use it 🤷‍♂️
There are two ways to open the program:

1) Via python

```bash
# Opens file using your python version
python -m location/of/.py/file
```
<br>

2) Via the .exe

```bash
# Opens the file by executing the .exe in the terminal
open location/of/.exe./file
```

<br>



## Dependencies 📊
You absolutelty need to have youtube-dl and ffmpeg tools installed. Otherwise, the program won't simply work. You can installed them with pip using the following commands:

```bash
pip install youtube_dl
```
```bash
pip install ffmpeg
```
<br>

Don't have pip? You can download it running this command:
<br>
<h3>Linux & MacOs</h3>

```bash
python -m ensurepip --upgrade
```

<h3>Windows</h3>

```bash
py -m ensurepip --upgrade
```
<br>

You don't have python either? You can download it <a href="https://www.python.org/downloads/" target="_blank">here</a>.

<br>

## License 🔒

[❯ Read the license here →](LICENSE.md) 📄

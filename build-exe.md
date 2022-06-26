# Compile Youtube-dl Terminal Gui
If you want to compile _Youtube-dl Terminal Gui_ into an .exe file, follow the following guide on how to do so.

<br>

## Requirements
1. PyInstaller 🛠
2. pip 🚚 (in case you don't have PyInstaller package installed)
3. Python3 🐍

<br>

In case you don't have Pyinstaller, you can download it with pip using:

```bash
# Run this command in your terminal/console
pip install pyinstaller
```

<br>

## Compile with PyInstaller

This will compile the program into a .exe you can run.
Depending on the folder you are located in the terminal, it will compile there.

For example:
```shell
YourUsername Desktop % (PyInstaller will compile program in ~/Desktop)
```
<br>

<img src="./public/img/hr.png">

<br>

✅ **Life pro tip**: You can check the directory you are in by running "pwd" in the terminal/console.

Example:

```shell
YourUsername Desktop % pwd

(The current path you are in)
```
<br>

<img src="./public/img/hr.png">

<br>

So, to compile the program into an .exe, run the following PyInstaller command:

```bash
pyinstaller --onefile [folder path of ytdl-tgui or file path of __main__.py] --name ytdl-tgui --hiddenimport=libiomp5.dylib
```
<br>

***Please note that compilation time may vary from machine to machine!**

After running Pyinstaller, you are going to see that some files and folders were created. Don't worry too much about it. We are only going to care about a folder called 'dist'. Inside of which, you are going to find the .exe.


From there, you can cut and paste the resulting .exe wherever you want, and run it just like any .exe file.

<br>

## An error ocurred, what should I do?!
Since we are using PyInstaller to compile _Youtube-dl Terminal Gui_, any error you encounter while attempting to compile may come directly from PyInstaller itself, and not from _Youtube-dl Terminal Gui_. 

You are encouraged to look on the internet for ways on how to solve any PyInstaller error, as there is a lot of info about PyInstaller online, but be aware that most problems you may encounter while compiling are because of some dependency that PyInstaller needs that's missing on your machine.

However, you are also welcome to open an [issue](https://github.com/AsleyR/ytdl-tgui/issues) at the ytdl-tgui repo. I'll gladly look at the problem and help you out 🙃.
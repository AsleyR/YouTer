# Compile Youtube-dl Terminal Gui With PyInstaller
If you want to compile Youtube-dl Terminal Gui into an .exe file, follow the following guide on how to do so.

---

## Requirements
1. PyInstaller 🛠
2. pip 🚚 (in case you don't have PyInstaller package installed)
3. Python3 🐍

<br>

In case you don't have Pyinstaller, you can download it with pip using the following command:

```bash
# Run this command in your terminal/console
pip install pyinstaller
```


## Compile with PyInstaller

This will compile the program into a .exe you can run.
Depending on the folder you are located in the terminal, it will output the resulting files there.

For example:
```shell
YourUsername Desktop % (PyInstaller will output the resulting files  in ~/Desktop)
```

---


✅ **Life pro tip**: You can check the current directory you are in by running `pwd` in the terminal/console.

For example:

```shell
YourUsername Desktop % pwd

/home/example-user/Desktop/Example-Folder
```
---

<br>

***Please note that compilation time may vary from machine to machine!**

So, to compile the program into an .exe, run the following PyInstaller command:

```bash
pyinstaller --onefile [folder path of ytdl-tgui] --name ytdl-tgui --hiddenimport=libiomp5.dylib
```
<br>


After running Pyinstaller, you are going to see that some files and folders are going to be created in your current directory. 

Don't worry about it. Of them all, we're only going to care about a folder named 'dist', since it's inside tis folder that we're going to find the resulting compiled .exe version of the program.

From there, you can cut and paste the resulting .exe wherever you want, and run it just like any .exe file.

## What does PyInstaller command do?

PyInstaller is a python package that seems kind of daunting at first. However, once you get the hang of it, you'll see that it's actually a piece of cake.

So to show this, let me explain step by step what does each part of the command we input above does.

Let's start with the base, `pyinstaller`, this part tells the terminal we want to run the pyinstaller CLI.

Next, we continue with `--onefile`, this part tells PyInstaller to only output the program as a single file. If we weren't to include this option, PyInstaller would compile the program inside a directory along all of the program's dependencies. In other words, this keyword tells PyInstaller to make the program portable.

Then we have `[folder path of ytdl-tgui]`, which tells PyInstaller the location of the python file you want to compile.

The following option, `--name ytdl-tgui`, is an optional parameter. It tells PyInstaller to change the filename of the output file. Right now, the commands tells PyInstaller to output the resulting .exe with the name 'ytdl-tgui' because that's the name of the program, but to be honest, you can change the name to anything you want and the program will still work.

Last in the list we have the `--hiddenimport=libiomp5.dylib` option. Personally, I wouldn't mess with this part of the command, as this is something of a precaution. When I was developing the program, PyInstaller, for some reason I don't know, refused to import this very crucial library into the resulting file. So, `--hiddenimport` does that, it let you manually import libraries into the compilation of the file. In this case, 'libiomp5.dylib' is a file found in the Intel OpenMP library that was needed in the compilation of Youtube-dl terminal gui.


## An error ocurred, what should I do?!
Since we are using PyInstaller to compile **Youtube-dl terminal gui**, any error you encounter while attempting to compile may be result of PyInstaller itself, and not of ytdl-tgui. 

You are encouraged to look on the internet for ways on how to solve any PyInstaller error you may face, as there is a lot of info about PyInstaller online, but be aware that most problems you may encounter while compiling are results of some dependency that PyInstaller needs that's missing on your machine.

However, you are also welcome to open a [new issue](https://github.com/AsleyR/ytdl-tgui/issues). I'll gladly look at the problem and help you out if I can 🙃.
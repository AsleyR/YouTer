<div align="center">
  <img src="https://raw.githubusercontent.com/AsleyR/YouTer/main/YouTer/public/img/YouTer%20Logo%20500-200.png" width="450">
</div>

<br>

YouTer is a small terminal-based gui program that simplifies youtube-dl into a more user-friendly experience for downloading youtube videos and audios in mp4 or mp3 formats. There is also an option to enter your own custom youtube-dl commands.

<br>

<h2> Table of contents</h2>

- [Features](#features)
- [Installation](#installation)
  - [Using pip](#using-pip)
  - [From Source](#from-source)
- [Usage](#usage)
  - [Pip](#pip)
  - [Manually](#manually)
- [Other](#other)
  - [Dependencies](#dependencies)
  - [Pip installation](#pip-installation)
- [How does the program work?](#how-does-the-program-work)
- [Contributions](#contributions)
- [License](#license)

<br>

## Features

With YouTer, you can download any YouTube video in any quality (only if the video has the selected quality available), or in the best possible quality.

Further, YouTer also allows you to take any YouTube video and download only the audio from it.

## Installation

### Using pip

YouTer can be installed using pip, along with all the program dependencies it needs to work. 

To download YouTer with pip using the following command:

```python
pip install YouTer
```

### From Source

1. Clone the repo into your local machine and _voilá_!

<br>

<div align="center">
<img src="https://raw.githubusercontent.com/AsleyR/YouTer/main/YouTer/public/img/clone_repo_guide.gif" width="500">
</div>

<br>

---

## Usage

There are several ways in which you can open the program.

### Pip

If YouTer was installed with pip, you can run the program in the terminal by simple writing `youter` in the terminal. The program will then be executed.

---

### Manually

Another way you can run the program is by opening either the module folder installed by pip, or the cloned folder from the repo. Then, once inside the folder, simply run the python file as a module with the following command:

```python
python3 -m YouTer
```

## Other

### Dependencies
YouTer uses the youtube-dl and ffmpeg packages in the background. To install them, you can run the following commands:

```bash
# Installs youtube_dl
pip install youtube_dl
```
```bash
# Installs ffmpeg
pip install ffmpeg
```
<br>

Don't have pip? Scroll down a little to see how to install it.

---
### Pip installation

<h4>Linux & MacOs</h4>

```bash
python3 -m ensurepip
```

<h4>Windows</h4>

```bash
py -m ensurepip
```
Please note that the installation of pip in windows can sometimes be... _complicated_. If you are having problems making pip work, I recommend you this [video guide](https://youtu.be/c_qNC1lL4qA) on how to install it.

<br>

You don't have python either? You can download it from the oficial website <a href="https://www.python.org/downloads/" target="_blank">here</a>.

## How does the program work?
**YouTer** is simply a kind of gui wrapper of the youtube-dl command tool. A good way to explain how it works would be like this:

<br>
<div align="center">
<img src="https://raw.githubusercontent.com/AsleyR/YouTer/main/YouTer/public/img/YouTer%20Explained.svg" width=250>
</div>

<br>

So basically, any command that works in youtube-dl works with this program too. If you check the `__main__.py` file, you may find that **YouTer** works by simply running youtube-dl commands in the background.

That's why there's an option inside the program to enter your custom youtube-dl commands, for those who want more control over the output command.

## Contributions
Any type of contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first before all.

## License

[❯ Read the license here →](LICENSE.md) 🔏

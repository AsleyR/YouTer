from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.1'
DESCRIPTION = 'Terminal based gui program that downloads youtube videos in mp4 or mp3 formats.'
LONG_DESCRIPTION = ''

# Setting up
setup(
    name="YouTer",
    version=VERSION,
    author="Asley R.",
    author_email="asleyrobleto@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['youtube_dl', 'ffmpeg'],
    keywords=['python', 'video', 'audio', 'download', 'terminal'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

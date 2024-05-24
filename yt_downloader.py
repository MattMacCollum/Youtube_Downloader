from pytube import YouTube
from sys import argv
from pytube.cli import on_progress
import sys
import os


url = input('Enter Youtube video URL: ')
yt = YouTube(url, on_progress_callback=on_progress)

down = yt.streams.get_highest_resolution()

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
pth = desktop + '/Youtube Download/'

if os.path.exists(pth) == False:
    os.makedirs(pth)
    down.download(pth)
else:
    down.download(pth)

from pytube import YouTube
from sys import argv
from pytube.cli import on_progress
import sys
import os
import tkinter
import customtkinter


# Sys settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')


def srt_download():
    ytlink = link.get()
    yt_obj = YouTube(ytlink)
    vid = yt_obj.streams.get_highest_resolution()

    desktop = os.path.join(os.path.join(
        os.path.expanduser('~')), 'Desktop')
    pth = desktop + '/Youtube Download/'

    if os.path.exists(pth) == False:
        os.makedirs(pth)
        vid.download(pth)
    else:
        vid.download(pth)

    print("Exception occurred")

    print("Download finished")


# initialise app frame
app = customtkinter.CTk()
app.geometry('740x480')
app.title('Youtube Downloader')


# UI elems
ttl = customtkinter.CTkLabel(app, text="Youtube Link")
ttl.pack(padx=10, pady=10)

url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=250, height=40, textvariable=url)
link.pack()


dwnld = customtkinter.CTkButton(app, text='Download', command=srt_download)
dwnld.pack(padx=10, pady=10)

# Run the application
app.mainloop()

'''
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
'''

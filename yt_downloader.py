from pytube import YouTube
from sys import argv
from pytube.cli import on_progress
import sys
import os
import tkinter
import customtkinter

from pytube.innertube import _default_clients

_default_clients["ANDROID_MUSIC"] = _default_clients["WEB"]


# Sys settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')


def srt_download():
    try:
        ytlink = link.get()
        yt_obj = YouTube(ytlink, on_progress_callback=on_progress)
        vid = yt_obj.streams.get_highest_resolution()

        ttl.configure(text=yt_obj.title)

        vid.download(pth)

        finish.configure(text='Download Finished')

    except:
        finish.configure(
            text='Exception occcure during download', text_color='red')


desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
pth = desktop + '/Youtube Download/'

if os.path.exists(pth) == False:
    os.makedirs(pth)

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

finish = customtkinter.CTkLabel(app, text=" ")
finish.pack()

# Run the application
app.mainloop()

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

        ttl.configure(text=yt_obj.title, font_weight="bold")
        finish.configure(text="")
        vid.download(pth)

        finish.configure(text='Download Finished', text_color='white')

    except:
        finish.configure(text='Exception occcured during download', text_color='red')

def cncl():
    app.destroy()


def on_progress(stream, chunk, bytes_remaining):
    sizetotal = stream.filesize
    bytes_downloaded = sizetotal - bytes_remaining
    percent = bytes_downloaded/bytes_remaining * 100
    progress_per.configure(text=str(int(percent)) + '%')
    progress_per.update()

    progressbar.set(float(percent)/100)


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


#Progress bar
progress_per = customtkinter.CTkLabel(app, text="0%")
progress_per.pack()

progressbar = customtkinter.CTkProgressBar(app, width=200)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

#Download Button
dwnld = customtkinter.CTkButton(app, text='Download', command=srt_download)
dwnld.pack(padx=10, pady=10)


#Cancel Button
cancel = customtkinter.CTkButton(app, text="Cancel", command=cncl)
cancel.pack(padx=10, pady=10)

finish = customtkinter.CTkLabel(app, text=" ")
finish.pack()


# Run the application
app.mainloop()

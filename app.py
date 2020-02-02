import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("450x350")

directory = askdirectory()
os.chdir(directory)  # change the directory to a specified path.

# returns a list containing a name of the entries in the specified path
songList = os.listdir()
playlist = tkr.Listbox(musicplayer, font="Helvetica 12 bold", bg="white", fg="black",
                       selectmode=tkr.SINGLE)  # this will display a list of the songs

# Each time we loop, we select a song and the position of the song will increase
for item in songList:
    position = 0
    playlist.insert(position, item)
    position = position + 1

pygame.init()
pygame.mixer.init()


# Create functions to control play, stop, pause buttons

# Play button
def play():
    # Get the active state. Basically ACTIVE is "this" keyword in js
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


# creating the actual buttons
PlayBtn = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                     bg="#1DB954", text="PLAY", fg="#fff", command=play)

StopBtn = tkr.Button(musicplayer, width=5, height=3,
                     font="Helvetica 12 bold", bg="#a11919", fg="#fff", text="STOP", command=stop)

PauseBtn = tkr.Button(musicplayer, width=5, height=3,
                      font="Helvetica 12 bold", bg="#9090ee", fg="#fff", text="PAUSE", command=pause)

UnpauseBtn = tkr.Button(musicplayer, width=5, height=3,
                        font="Helvetica 12 bold", bg="#ee90ee", fg="#fff", text="UNPAUSE", command=unpause)


# Display song title

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Helvetica 12 bold", textvariable=var)

songtitle.pack()  # this will arrange the song titles inside the widget
PlayBtn.pack(fill="x")
StopBtn.pack(fill="x")
PauseBtn.pack(fill="x")
UnpauseBtn.pack(fill="x")
playlist.pack(fill="both", expand="yes")

musicplayer.mainloop()

import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("450 X 350")

directory = askdirectory()
os.chdir(directory)  # change the directory to a specified path.

# returns a list containing a name of the entries in the specified path
songList = os.listd()
playlist = tkr.Listbox(musicplayer, font="Helvetica 12 bold", bg="white",
                       selectmode=tkr.SINGLE)  # this will display a list of the songs

# Each time we loop, we select a song and the position of the song will increase
for item in songList:
    position = 0
    playlist.insert(position, item)
    position = position + 1

pygame.init()
pygame.mixer.init()


#Create functions to control play, stop, pause buttons

#Play button 
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE)) #Get the active state. Basically ACTIVE is "this" keyword in js 
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()
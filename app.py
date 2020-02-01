import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("450 X 350")

directory = askdirectory()
os.chdir(directory)#change the directory to a specified path.

songList = os.listd() #returns a list containing a name of the entries in the specified path
playlist = tkr.Listbox(musicplayer ,font="Helvetica 12 bold",bg="white", selectmode = tkr.SINGLE ) # this will display a list of the songs 






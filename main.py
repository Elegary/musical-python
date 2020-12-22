#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  main.py

from tkinter import *
from sound import *
from partition import *
from  time  import  sleep

import  simpleaudio  as  sa
import numpy as np

def show_msg():
    # Example for a LA noire
    print(get_frequency_for_note("LA"))
    print(get_duration_for_figure("n"))
    read_database("partitions.txt")


window = Tk()
window.title("Musical Python")
window.minsize(800,600)
window.iconbitmap("assets/music_note.ico")
window.config(bg="#191414")

frame= Frame(window, bg="#1DB954")
frame.config(width=500, height=500)

frame.pack(expand=YES)

btn = Button(frame, text="Play a sound", font=("Courrier",25), bg="#191414", fg="#FFFFFF", command=show_msg)
btn.pack(pady=10, side='bottom', fill=X)
btn.place(x=20, y=20)

window.mainloop()
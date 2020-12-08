#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This the part of musical-python
#  main.py created on 8/12/2020

from tkinter import *

def show_msg():
    print("Playing a sound")

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
#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  main.py

from tkinter import *
from sound import *
from partition import *
from  time  import  sleep

import  simpleaudio  as  sa
import numpy as np

def show_msg(title):
    # Example for a LA noire
    '''
    database = read_database("partitions.txt")
    #print(database) #renvoie les partitions dans une liste
    for partition in database:
        print(partition["title"])
        sleep(1)
    '''
    print(title)


window = Tk()
window.title("Musical Python")
window.minsize(1000, 800)
window.iconbitmap("assets/music_note.ico")
window.config(bg="#191414")

top_bar = Frame(window, bg="#1DB954")
top_bar.config(height=80)
top_bar.pack(fill=X)

title_top_bar = Label(top_bar, text="Musical Python", font=("Segoe UI", 30), fg="#FFFFFF", bg="#1DB954")
title_top_bar.pack()
title_top_bar.place(x=50, y=8)
logo_top_bar = PhotoImage(file="assets/music_note.png")

canvas_app_bar = Canvas(top_bar, width=50, height=50, bg="#1DB954", bd=0, highlightthickness=0)
canvas_app_bar.create_image(36, 36, image=logo_top_bar)
canvas_app_bar.pack()
canvas_app_bar.place(x=-5, y=5)

frame_content = Frame(window, bg="#191414")
frame_content.place(x=0, y=80)
frame_content.pack(fill=BOTH)

database = read_database("partitions.txt")

for partition in database:
    title = partition["title"]
    parsed_partition = parse_partition(partition)

    my_frame = Frame(frame_content, bg="#414141")
    my_frame.config(width=1800, height=111)

    title = Label(my_frame, text=title, font=("Segoe UI", 30), fg="#FFFFFF", bg="#414141", cursor="hand2")
    title.bind("<Button-1>", lambda e,infos=parsed_partition:play_partition_parsed(infos))
    title.pack()
    title.place(x=25, y=23)

    my_frame.grid(pady=15, padx=73)


window.mainloop()
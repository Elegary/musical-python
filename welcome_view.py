#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  welcome_view.py

from tkinter import *
from show_view import *
from PIL import ImageTk, Image

def load_welcome_view(window, views):
    container = Frame(window)
    container.config(bg="#191414")

    welcome_label = Label(container, text="Welcome to musical Python ! \nA Python project created by Romain CAUSSIGNAC & Matthieu VIVIER", font=("Segoe UI",30), fg="#1DB954", bg="#191414")
    btn_get_started = Button(container, text="Get started", font=("Segoe UI",35), fg="white", bg="#1DB954", width=33, height=2, cursor="hand2", bd=5, relief=SOLID, command=lambda: show_view(views, "partitions_list_view"))

    welcome_label.pack(fill=BOTH, expand=1)
    btn_get_started.pack(expand=1)

    img = ImageTk.PhotoImage(file=r"book.png")
    title_bis = Label(container, image=img, bg="#1DB954")
    title_bis.pack()

    return container
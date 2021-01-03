#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  partition_details_view.py

from tkinter import *

from show_view import show_view


def load_partition_details_view(window, views):
    container = Frame(window, bg="#191414")

    top_bar = Frame(container, bg="#1DB954")
    top_bar.pack(fill=X)
    top_bar.config(height=80)

    title_top_bar = Label(top_bar, text="Musical Python", font=("Segoe UI", 30), fg="#FFFFFF", bg="#1DB954")
    title_top_bar.pack()
    title_top_bar.place(x=50, y=8)
    logo_top_bar = PhotoImage(file="assets/music_note.png")

    canvas_app_bar = Canvas(top_bar, width=30, height=30, bg="#1DB954")
    canvas_app_bar.create_image(36, 36, image=logo_top_bar)
    canvas_app_bar.pack()
    canvas_app_bar.place(x=0, y=0)

    btn_infos = Button(top_bar, text="About...", font=("Segoe UI", 13), fg="#FFFFFF", bg="#1DB954")
    btn_infos.pack(side=RIGHT, padx=15, pady=20)

    btn_back = Button(top_bar, text="Home", font=("Segoe UI", 13), fg="#FFFFFF", bg="#1DB954", command=lambda: show_view(views, "partitions_list_view"))
    btn_back.pack()
    btn_back.place(x=400, y=15)

    main_frame = Frame(container, bg="#191414")
    main_frame.place(x=0, y=80)
    main_frame.pack(fill=BOTH, expand=1)

    title_label = Label(container, text=views["partition"]["title"], font=("Segoe UI", 30), fg="#FFFFFF", bg="#191414")
    title_label.pack(pady=10)

    details = Frame(container, bg="#1DB954")
    details.config(width=1500, height=500)
    details.pack(padx=15, pady=50)

    partition_label = Label(details, text=views["partition"]["infos"], font=("Segoe UI",30), fg="white", bg="#1DB954", wraplengt=1000, height=10)
    partition_label.config(width=50)
    partition_label.pack()

    actions = Frame(container, bg="#1DB954")
    actions.config(width=1500, height=130)
    actions.pack(padx=15, pady=50)

    return container
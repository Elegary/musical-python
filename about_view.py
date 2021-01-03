#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  about_view.py

from tkinter import *

from show_view import show_view


def load_about_view(window, views):
    container = Frame(window)

    top_bar = Frame(container, bg="#1DB954")
    top_bar.pack(fill=X)
    top_bar.config(height=80)

    title_top_bar = Label(top_bar, text="About this project...", font=("Segoe UI", 30), fg="#FFFFFF", bg="#1DB954")
    title_top_bar.pack()
    title_top_bar.place(x=50, y=8)
    logo_top_bar = PhotoImage(file="assets/music_note.png")

    canvas_app_bar = Canvas(top_bar, width=30, height=30, bg="#1DB954")
    canvas_app_bar.create_image(36, 36, image=logo_top_bar)
    canvas_app_bar.pack()
    canvas_app_bar.place(x=0, y=0)

    main_frame = Frame(container, bg="#191414")
    main_frame.place(x=0, y=80)
    main_frame.pack(fill=BOTH, expand=1)

    btn_back = Button(main_frame, text="Get back home", font=("Segoe UI", 20), fg="#FFFFFF", bg="#1DB954", command=lambda: show_view(views, "partitions_list_view"))
    btn_back.pack(pady=20)

    details = Frame(main_frame, bg="#1DB954")
    details.pack(padx=15, pady=15)

    about_text = "Created by Matthieu VIVIER & Romain CAUSSIGNAC \n" \
                 "Created during a school project for EFREI PARIS university.\n" \
                 "This project is OpenSource. Source code will be available on Github.\n\n" \
                 "Originally created with the Font Awesome Icons\n" \
                 "See https://fontawesome.com/license for license.\n" \
                 "No changes where made to icons."

    about_label = Label(details, text=about_text, font=("Segoe UI",25), fg="white", bg="#1DB954", wraplengt=1300)
    about_label.pack(padx=30, pady=30)

    return container
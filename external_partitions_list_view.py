#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  external_partitions_list.py

from tkinter import *

from partition import *
from show_view import show_view

def load_partition_view(views, partition):
    views["partition"] = partition
    show_view(views, "partition_details_view")


def load_external_partitions_list_view(window, views):
    container = Frame(window)

    top_bar = Frame(container, bg="#1DB954")
    top_bar.pack(fill=X)
    top_bar.config(height=80)

    title_top_bar = Label(top_bar, text="Currently external Database", font=("Segoe UI", 30), fg="#FFFFFF", bg="#1DB954")
    title_top_bar.pack()
    title_top_bar.place(x=50, y=8)
    logo_top_bar = PhotoImage(file="assets/music_note.png")

    canvas_app_bar = Canvas(top_bar, width=30, height=30, bg="#1DB954")
    canvas_app_bar.create_image(36, 36, image=logo_top_bar)
    canvas_app_bar.pack()
    canvas_app_bar.place(x=0, y=0)

    btn_infos = Button(top_bar, text="About...", font=("Segoe UI", 13), fg="#FFFFFF", bg="#191414", command=lambda: show_view(views, "about_view"))
    btn_infos.pack(side=RIGHT, padx=15, pady=20)

    btn_back = Button(top_bar, text="Home", font=("Segoe UI", 13), fg="#FFFFFF", bg="#191414", command=lambda: show_view(views, "partitions_list_view"))
    btn_back.pack()
    btn_back.place(x=600, y=15)

    main_frame = Frame(container, bg="#191414")
    main_frame.place(x=0, y=80)
    main_frame.pack(fill=BOTH, expand=1)

    canvas_view = Canvas(main_frame, bd=0, highlightthickness=0)
    canvas_view.pack(side=LEFT, fill=BOTH, expand=1)
    canvas_view.config(bg="#191414")

    scrollbar = Scrollbar(main_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas_view.configure(yscrollcommand=scrollbar.set)
    canvas_view.bind("<Configure>", lambda e: canvas_view.configure(scrollregion = canvas_view.bbox("all")))

    frame_content = Frame(canvas_view, bg="#191414")

    def on_mousewheel(event):
        canvas_view.yview_scroll(int(-1*(event.delta/120)), "units")


    database = read_database(views["path"])

    for partition in database:
        title = partition["title"]
        parsed_partition = parse_partition(partition)

        my_frame = Frame(frame_content, bg="#414141")
        my_frame.config(width=1804, height=111)

        title = Label(my_frame, text=title, font=("Segoe UI", 30), fg="#FFFFFF", bg="#414141", cursor="hand2")
        title.bind("<Button-1>", lambda e,partition=partition:load_partition_view(views, partition))
        title.pack()
        title.place(x=25, y=23)

        img = PhotoImage(file="assets/book.png")

        title_bis = Canvas(my_frame, width=64, height=64, bg="#414141")
        title_bis.create_image(64, 64, image=img)
        title_bis.pack()
        title_bis.place(x=555, y=23)

        my_frame.grid(pady=15, padx=50)

    scrollbar.config(command=canvas_view.yview)
    canvas_view.bind_all("<MouseWheel>", on_mousewheel)
    canvas_view.create_window((0,0), window=frame_content, anchor="nw")

    return container
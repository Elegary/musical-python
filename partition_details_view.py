#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  partition_details_view.py

from tkinter import *

from partition import *
from show_view import show_view

def pre_play_partition(partition_parsed):
    if apply_inversion_effect.get():
        partition_parsed = inverse_partition(partition_parsed)

    if apply_transpose_effect.get():
        partition_parsed = transpose_partition(partition_parsed, k=5)

    play_partition_parsed(partition_parsed)

def load_partition_details_view(window, views):
    container = Frame(window, bg="#191414")

    # Using global modifier lets us to access the options Boolean outside the current function
    global apply_transpose_effect
    apply_transpose_effect = BooleanVar()
    apply_transpose_effect.set(False)

    global apply_inversion_effect
    apply_inversion_effect = BooleanVar()
    apply_inversion_effect.set(False)


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

    btn_infos = Button(top_bar, text="About...", font=("Segoe UI", 13), fg="#FFFFFF", bg="#191414")
    btn_infos.pack(side=RIGHT, padx=15, pady=20)

    btn_back = Button(top_bar, text="Home", font=("Segoe UI", 13), fg="#FFFFFF", bg="#191414", command=lambda: show_view(views, "partitions_list_view"))
    btn_back.pack()
    btn_back.place(x=400, y=15)

    main_frame = Frame(container, bg="#191414")
    main_frame.place(x=0, y=80)
    main_frame.pack(fill=BOTH, expand=1)

    title_label = Label(main_frame, text="Title : " + views["partition"]["title"], font=("Segoe UI", 30), fg="#FFFFFF", bg="#191414")
    title_label.pack()

    infos = Label(main_frame, text="Partition info : ", font=("Segoe UI", 25), fg="#FFFFFF", bg="#191414")
    infos.pack()

    details = Frame(main_frame, bg="#1DB954")
    details.config(width=1500, height=500)
    details.pack(padx=15, pady=15)

    partition_label = Label(details, text=views["partition"]["infos"], font=("Segoe UI",30), fg="white", bg="#1DB954", wraplengt=1000, height=10)
    partition_label.config(width=50)
    partition_label.pack()

    actions = Frame(container, bg="#1DB954")
    actions.config(width=1500, height=130)
    actions.pack(padx=15, pady=50)

    partition_parsed = parse_partition(views["partition"])

    btn_back = Button(actions, text="Play", font=("Segoe UI", 18), fg="#FFFFFF", bg="#191414", command=lambda: pre_play_partition(partition_parsed))
    btn_back.config(height=2, width=10)
    btn_back.pack()
    btn_back.place(x=30, y=20)

    inverse_option = Checkbutton(actions, text="Apply inversion effect", font=("Segoe UI", 15), bg="#1DB954", activebackground="#1DB954", var=apply_inversion_effect)
    inverse_option.pack()
    inverse_option.place(x=200, y=15)

    transpose_option = Checkbutton(actions, text="Apply transposition effect", font=("Segoe UI", 15), bg="#1DB954", activebackground="#1DB954", var=apply_transpose_effect)
    transpose_option.pack()
    transpose_option.place(x=200, y=60)

    return container
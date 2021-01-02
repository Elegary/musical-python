#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  main.py

from tkinter import *

from views import *

from show_view import *

window = Tk()
window.title("Musical Python")
window.minsize(1300, 800)
window.iconbitmap("assets/music_note.ico")
window.config(bg="#191414")

Grid.rowconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 0, weight=1)

views = load_views(window)

for key, view in views.items():
    view.grid(row=0, column=0, sticky='nsew')

show_view(views, "welcome_view")

window.mainloop()
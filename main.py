#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  main.py

from tkinter import *

from views import *

from show_view import *

# We create a window using the Tkinter Library
window = Tk()
window.title("Musical Python")
window.minsize(1300, 800)
window.iconbitmap("assets/music_note.ico")
window.config(bg="#191414")

# We configure the window with a grid system (used to switch between views)
Grid.rowconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 0, weight=1)

# We load the views (assign each view to a key in a dictionnary
views = load_views(window)

# We use grid to have multiple views, and switch between the views
for key, view in views.items():
    if key != "path":
        view.grid(row=0, column=0, sticky='nsew')

# We show the "Welcome" screen to the user
show_view(views, "welcome_view")

window.mainloop()
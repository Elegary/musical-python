#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  show_view.py

def show_view(views, view_name):
    view = views[view_name]
    view.tkraise()
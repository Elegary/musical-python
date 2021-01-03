#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  views.py

from partitions_list_view import load_partitions_list_view
from welcome_view import load_welcome_view
from external_partitions_list import load_external_partitions_list_view

views = {}
current_window = ""

def load_views(window):
    current_window = window
    views["path"] = "partitions.txt"
    views["welcome_view"] = load_welcome_view(window, views)
    views["external_partitions_list_view"] = load_external_partitions_list_view(window, views)
    views["partitions_list_view"] = load_partitions_list_view(window, views)

    return views

def updatePath():
    print(views["path"])
    views["external_partitions_list_view"] = load_external_partitions_list_view(current_window, views)
    views["external_partitions_list_view"].grid(row=0, column=0, sticky='nsew')
    views["partitions_list_view"] = load_partitions_list_view(current_window, views)
    views["partitions_list_view"].grid(row=0, column=0, sticky='nsew')
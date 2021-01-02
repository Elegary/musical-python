#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  views.py

from partitions_list_view import load_partitions_lists_view
from welcome_view import load_welcome_view

views = {}

def load_views(window):

    views["welcome_view"] = load_welcome_view(window, views)
    views["partitions_list_view"] = load_partitions_lists_view(window, views)

    return views
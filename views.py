#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  views.py

from partitions_list_view import load_partitions_list_view
from welcome_view import load_welcome_view
from external_partitions_list import load_external_partitions_list_view
from partition_details_view import load_partition_details_view

views = {}
current_window = ""

def load_views(window):
    current_window = window
    views["path"] = "partitions.txt"
    views["partition"] = {"title": "Title", "infos": "Data"}
    views["is_in_database"] = True
    views["welcome_view"] = load_welcome_view(window, views)
    views["partition_details_view"] = load_partition_details_view(window, views)
    views["external_partitions_list_view"] = load_external_partitions_list_view(window, views)
    views["partitions_list_view"] = load_partitions_list_view(window, views)

    return views

# These three functions forces the view to be re rendered with the new values
def update_partitions_list_view():
    views["partitions_list_view"] = load_partitions_list_view(current_window, views)
    views["partitions_list_view"].grid(row=0, column=0, sticky='nsew')

def updatePath():
    print(views["path"])
    views["external_partitions_list_view"] = load_external_partitions_list_view(current_window, views)
    views["external_partitions_list_view"].grid(row=0, column=0, sticky='nsew')
    update_partitions_list_view()

def updatePartition():
    views["partition_details_view"] = load_partition_details_view(current_window, views)
    views["partition_details_view"].grid(row=0, column=0, sticky='nsew')
    update_partitions_list_view()
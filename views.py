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
    views["partition"] = {"title": "Joyeux Anniversaire", "infos": "SOLc p Zc SOLn LAn SOLn DOn Zc SIb SOLc p Zc SOLn LAn SOLn REn Zc DOb SOLc p Zc SOLn SOLn MIn DOn Zc SIn LAn FAc p Zc FAn MIn DOn REn DOr"}
    views["welcome_view"] = load_welcome_view(window, views)
    views["partition_details_view"] = load_partition_details_view(window, views)
    views["external_partitions_list_view"] = load_external_partitions_list_view(window, views)
    views["partitions_list_view"] = load_partitions_list_view(window, views)

    return views

def updatePath():
    print(views["path"])
    views["external_partitions_list_view"] = load_external_partitions_list_view(current_window, views)
    views["external_partitions_list_view"].grid(row=0, column=0, sticky='nsew')
    views["partitions_list_view"] = load_partitions_list_view(current_window, views)
    views["partitions_list_view"].grid(row=0, column=0, sticky='nsew')

def updatePartition():
    views["partition_details_view"] = load_partition_details_view(current_window, views)
    views["partition_details_view"].grid(row=0, column=0, sticky='nsew')
    views["partitions_list_view"] = load_partitions_list_view(current_window, views)
    views["partitions_list_view"].grid(row=0, column=0, sticky='nsew')
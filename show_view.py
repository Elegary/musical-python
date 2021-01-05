#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  show_view.py

import views as vi

def show_view(views, view_name):
    # Checking if the destination view needs specific update
    if view_name == "external_partitions_list_view":
        views["is_in_database"] = False
        vi.updatePath()

    elif view_name == "partition_details_view":
        vi.updatePartition()

    elif view_name == "partitions_list_view":
        views["is_in_database"] = True
        views["path"] = "partitions.txt"
        vi.update_partitions_list_view()

    view = views[view_name]
    # Switching to the indicated view_name
    view.tkraise()
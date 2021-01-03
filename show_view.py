#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  show_view.py

import views as vi

def show_view(views, view_name):
    if view_name == "external_partitions_list_view":
        vi.updatePath()

    elif view_name == "partition_details_view":
        vi.updatePartition()

    view = views[view_name]
    view.tkraise()
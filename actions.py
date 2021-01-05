#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  markov_action.py

from pathlib import Path

from partition import *

from show_view import show_view

def load_partition_view(views, partition):
    views["partition"] = partition
    show_view(views, "partition_details_view")

def markov_action(views, version):
    db = read_database(views["path"])
    all_partitions = {"title": "", "infos": ""}

    nbr_notes = 0

    for partition in db:
        parsed = parse_partition(partition)
        # Counting number of notes
        for element in parsed:
            if element["type"] == "note":
                nbr_notes += 1
        all_partitions["infos"] += partition["infos"] + " "

    all_partitions["infos"] = all_partitions["infos"].rstrip()

    partition_parsed = parse_partition(all_partitions)
    matrix = markov_matrix(partition_parsed)

    length = int(nbr_notes / len(db))

    new_partition = {}

    if version == 1:
        new_partition["infos"] = generate_with_markov_v1(matrix, length)

    elif version == 2:
        new_partition["infos"] = generate_with_markov_v2(matrix, length)

    new_partition["title"] = f"[Generated with Markov V{version}] Style from {Path(views['path']).name}"

    views["is_in_database"] = False
    views["partition"] = new_partition
    show_view(views, "partition_details_view")
#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  partition.py
import copy

from sound import *
from  time  import  sleep

notes_list = ["do", "re", "mi", "fa", "sol", "la", "si"]

def read_database(path):
    partitions_list = []
    # Opening with encoding utf-8 to support accents and special letters
    f = open(path, "r", encoding='utf8')
    content = f.readlines()

    for i, line in enumerate(content):
        #print(line)
        if line.startswith("#"):
            # Get the title of the partition, with the number (we remove the \n new line character with rstrip() function)
            title_with_number = line.split("#")[1].rstrip().split(" ")
            # Remove first element of list string that contains the number of the partition
            title_with_number.pop(0)
            title = " ".join(title_with_number)
            # Partition infos is the next line (we remove the \n new line character with rstrip() function)
            infos = content[i + 1].rstrip()
            partition = {"title": title, "infos": infos}
            partitions_list.append(partition)
    # Return the partition list
    return partitions_list

def parse_partition(partition):
    partition_infos = []
    elements = partition["infos"].split(" ")

    for element in elements:
        # Check if it is a note
        if len(element) >= 3:
            if len(element) == 4:
                figure = element[3]
                note = element[0:3]
            else:
                figure = element[2]
                note = element[0:2]
            data = {"type": "note", "figure": figure, "note": note.lower()}
        # Check if it is a silence
        if len(element) == 2 and element[0] == 'Z':
            figure = element[1]
            data = {"type": "silence", "figure": figure}
        # Check if it is a prolongation
        if len(element) == 1 and element == 'p':
            # data = mutliply the last figure duration * 1,5
            data = {"type": "prolongation", "factor": 1.5}
        partition_infos.append(data)
    #print(partition_infos)
    return partition_infos

def play_partition_parsed(partition_parsed):
    print(markov_matrix(partition_parsed))
    print(inverse_partition(partition_parsed))
    for i, val, in enumerate(partition_parsed):
        if val["type"] == "note":
            frequency = get_frequency_for_note(val["note"])
            duration = get_duration_for_figure(val["figure"])
            if i != len(partition_parsed) - 1 and partition_parsed[i + 1]["type"] == "prolongation":
                duration *= partition_parsed[i + 1]["factor"]
            generate_sound(frequency, duration * 0.001)

        if val["type"] == "silence":
            duration = get_duration_for_figure(val["figure"])
            if i != len(partition_parsed) - 1 and partition_parsed[i + 1]["type"] == "prolongation":
                duration *= partition_parsed[i + 1]["factor"]
            sleep(duration * 0.001)


def markov_matrix(partition_parsed):
    markov_matrix = []

    for note in notes_list:
        stats = [0] * len(notes_list)

        for i, element in enumerate(partition_parsed):
            if element["type"] == "note" and element["note"] == note and i != len(partition_parsed) - 1:
                j = i + 1

                while j != len(partition_parsed) - 1 and partition_parsed[j]["type"] != "note":
                    j += 1

                if partition_parsed[j]["type"] == "note":
                    index = notes_list.index(partition_parsed[j]["note"])
                    stats[index] += 1

        markov_matrix.append(stats)

    return markov_matrix

def generate_with_markov(markov_matrix):
    pass

def transpose_partition(partition_parsed, k):
    partition_transposed = copy.deepcopy(partition_parsed)

    for element in partition_transposed:
        if element["type"] == "note":
            index = notes_list.index(element["note"])
            new_index = (index + k) % len(notes_list)
            element["note"] = notes_list[new_index]

    return partition_transposed

def inverse_partition(partition_parsed):
    partition_inverted = copy.deepcopy(partition_parsed)

    for element in partition_inverted:
        if element["type"] == "note":
            index = notes_list.index(element["note"])
            new_index  = (len(notes_list) - index) % len(notes_list)
            element["note"] = notes_list[new_index]

    return partition_inverted
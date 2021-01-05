#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  partition.py
import copy
import random
import turtle

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

def save_new_partition(partition, path):
    # Opening with encoding utf-8 to support accents and special letters
    # Opening with "a+" mode let us to append to file, not overwrite the file and also read (to check the number)
    f = open(path, "r", encoding='utf8')
    # the second latest file contains the last number of partition
    content = f.readlines()
    i = -1
    while not content[i].startswith("#"):
        i -= 1
    last_number = content[i].split("#")[1].split(" ")[0]
    f.close()

    f = open(path, "a", encoding='utf8')
    f.write(f"\n#{int(last_number) + 1} {partition['title']}\n")
    f.write(partition["infos"])
    f.close()

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
    # TURTLE ANIMATION OK, BUT IT WAS SLOVWER, SO TO ENABLE ANIMATION JUST UNCOMMENT THE COMMENTED LINES IN THIS FUNCTION
    '''
    s = turtle.getscreen()
    d = 0
    turtle.bgcolor("grey")
    colors = ["green", "orange", "yellow", "blue", "purple", "red"]
    x = 0
    '''

    for i, val, in enumerate(partition_parsed):
        if val["type"] == "note":
            frequency = get_frequency_for_note(val["note"])
            duration = get_duration_for_figure(val["figure"])
            if i != len(partition_parsed) - 1 and partition_parsed[i + 1]["type"] == "prolongation":
                duration *= partition_parsed[i + 1]["factor"]
            generate_sound(frequency, duration * 0.001)
            '''
            d += 1
            turtle.up()
            turtle.color(colors[x % 6])
            turtle.width(x / 100 + 1)
            turtle.down()
            turtle.forward(x)
            turtle.left(59)
            x = (x + 1) % 360
            '''

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

def generate_with_markov_v1(markov_matrix, number_of_notes):
    note = notes_list[random.randint(0, len(notes_list) - 1)]

    partition_generated = [note.upper() + "n"]

    for i in range(number_of_notes - 1):
        note_index = notes_list.index(note)
        note = generate_next_note(markov_matrix, note_index, v2=False)
        partition_generated.append(note.upper() + "n")

    return " ".join(partition_generated)

def generate_with_markov_v2(markov_matrix, number_of_notes):
    # First get the max occurrences
    index_note_with_max_occurences = 0 # do
    max_occurences = 0

    for i, note_stats in enumerate(markov_matrix):
        occurrences = 0

        for j, note_after_number in enumerate(note_stats):
            occurrences += note_after_number

        if occurrences > max_occurences:
            index_note_with_max_occurences = i
            max_occurences = occurrences

    note = notes_list[index_note_with_max_occurences]
    partition_generated = [note.upper() + "n"]
    for i in range(number_of_notes - 1):
        note_index = notes_list.index(note)
        note = generate_next_note(markov_matrix, note_index, v2=True)
        partition_generated.append(note.upper() + "n")

    return " ".join(partition_generated)


def generate_next_note(markov_matrix, note_index, v2):
    array_successor = []
    for index, occurences in enumerate(markov_matrix[note_index]):
        if occurences > 0:
            if v2:
                to_insert = [notes_list[index]] * occurences
                array_successor.extend(to_insert)
            else:
                array_successor.append(notes_list[index])

    return array_successor[random.randint(0, len(array_successor) - 1)]


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
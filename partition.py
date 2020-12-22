#  Copyright (c) Romain CAUSSIGNAC & Matthieu VIVIER
#  This is the part of musical-python
#  partition.py

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
    elements = partition.split(" ")
    for element in elements:
        # Check if it is a note
        if len(element) >= 3:
            if len(element) == 4:
                figure = element[3]
                note = element[0:2]
            else:
                figure = element[2]
                note = element[0:1]
        # Check if it is a silence
        if len(element) == 2 and element[0] == 'Z':
            figure_silence = element[1]
        # Check if it is a prolongation
        if len(element) == 1 and element == 'p':
            # mutliply the last figure duration * 1,5
            pass



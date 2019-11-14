#!/usr/bin/env python 

def get_max_from_train_datafile(file_name, separator=';', ignore_first=True):
    """
    Returns the station and max travelers from a structured file.

    The input file must be a csv file.

    :param file_name: the path to the file
    :param separator: the separator charater to use, default is semicolon
    :param ignore_first: should the first line be ignored, default is True
    :return: a tuple, first element is the station name and the secodn is the
    number of travelers
    """
    max_travelers = 0
    station = None

    with open(file_name) as data_file:
        if ignore_first:
            data_file.readline()


        for line in data_file:
            data = line.split(';')
            travelers = int(data[-1])
            if travelers > max_travelers:
                max_travelers = travelers
                station = data[0]

    return station, max_travelers

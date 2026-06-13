import pandas as pd

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
    train_data = pd.read_csv(file_name, sep=separator)

    result = train_data.loc[
        train_data['Montants'] == train_data['Montants'].max(),
        ['Nom gare', 'Montants']
    ]
    if len(result) == 1:
        station, count = result.iloc[0]
        return station, int(count)

    return result


def select_station_line(train_data: pd.DataFrame,
                        station: str, line: str) -> pd.DataFrame:
    return train_data.loc[(train_data['Nom gare'] == station)
                          & (train_data['Ligne'] == line)]


def order_chronologically(train_data: pd.DataFrame):
    horaires = {
        "Avant 6h": 0,
        "De 6h à 10h": 1,
        "De 10h à 16h": 2,
        "De 16h à 20h": 3,
        "Après 20h": 4,
    }

    return train_data.sort_values(by=["Date de comptage", "Tranche horaire"],
                                  key=lambda val: val
                                  if val.name != "Tranche horaire"
                                  else val.map(horaires))

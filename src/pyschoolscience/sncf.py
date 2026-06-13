import pandas as pd


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

import pandas as pd


def similarity(anime1, anime2):
    genres1 = set(anime1["Genres"].split(","))
    genres2 = set(anime2["Genres"].split(","))
    common = len(genres1.intersection(genres2))
    total = len(genres1.union(genres2))

    year1 = anime1["Premiered"]
    year2 = anime2["Premiered"]

    if year1 == year2:
        common += 1
    total += 1

    # eng_Name1 = set(anime1[tipo_nombre_grafo].split(" "))
    # eng_Name2 = set(anime2[tipo_nombre_grafo].split(" "))

    # common += len(eng_Name1.intersection(eng_Name2))
    # total += len(eng_Name1.union(eng_Name2))

    return common / total

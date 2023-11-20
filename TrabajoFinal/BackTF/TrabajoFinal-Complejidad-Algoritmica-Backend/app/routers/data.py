from app.utils.graph import Grafo
import pandas as pd

grafo = Grafo()
total_cargado = grafo.import_graph_from_file("app/assets/graph__file/grafo_anime.csv")


df_anime = pd.read_csv(
    "app/assets/dataset/anime-dataset-2023.csv",
    encoding="utf-8",
)
print("Tamaño del dataset: ", df_anime.shape)
print("Dataset cargado correctamente")

all_genres = df_anime["Genres"].str.split(", ")
lista_generos = []

for genres in all_genres:
    for genre in genres:
        if genre not in lista_generos:
            lista_generos.append(genre)

print("Generos cargados correctamente")
print("Generos: ", lista_generos)

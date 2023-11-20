from fastapi import APIRouter
from .data import grafo, df_anime
from .index import df_anime


# print(total_cargado)
# grafo.print_graph()

router = APIRouter()


@router.get("/anime/two_recomend/{start}/{end}")
async def dijkstra_shortest_path(start, end):
    """
    Encuentra el camino más corto entre dos animes utilizando el algoritmo de Dijkstra.

    Args:
        start (str): El anime de inicio.
        end (str): El anime de destino.

    Returns:
        dict: Un diccionario que contiene los animes recomendados y los animes consultados.
    """
    if start not in grafo.graph:
        return {"error": f"Anime '{start}' not found"}
    if end not in grafo.graph:
        return {"error": f"Anime '{end}' not found"}

    short_path, _ = grafo.dijkstra_shortest_path(start, end)

    if len(short_path) <= 4:
        short_path = _[:6]
        _ = _[6:]

    # buscar en df_anime los animes en short_path
    animes_encontrados = []
    for anime in df_anime.iterrows():
        if anime[1]["Name"] in short_path:
            animes_encontrados.append(anime[1])

    # Remove None values from the list
    animes_encontrados = [anime for anime in animes_encontrados if anime is not None]

    if short_path and _ is None:
        return {"error": "No se encontro el camino"}
    return {"animes_encontrados": animes_encontrados, "animes_consultados": _}


@router.get("/animes/setup")
async def setup():
    """
    Usa el algorimo de Kruskal para generar unas recomendaciones iniciales de los animes.

    Returns:
        animes: {
            0: {
                Info anime 1
            }
            ...
        }
    """
    resultado = grafo.kruskal()

    resultado_list = []
    for anime in df_anime.iterrows():
        if anime[1]["Name"] in resultado:
            resultado_list.append(anime[1])

    return {"animes": resultado_list}

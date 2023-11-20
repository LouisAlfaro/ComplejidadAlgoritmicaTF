from fastapi import APIRouter
from .data import grafo, df_anime, lista_generos
from .graph_route import grafo
from difflib import get_close_matches


def search_anime(anime_name: str):
    """
    Busca un anime en el dataframe df_anime por su nombre.

    Args:
    anime_name (str): El nombre del anime a buscar.

    Returns:
    Si se encuentra el anime, retorna la fila correspondiente del dataframe.
    Si no se encuentra el anime, retorna None.
    """
    for index, row in df_anime.iterrows():
        if row["Name"] == anime_name:
            return row
    return {"error": "Anime no encontrado"}


def search_anime_by_id(id: int):
    """
    Busca un anime en el dataframe df_anime por su id.

    Args:
        id (int): El id del anime a buscar.

    Returns:
        dict: Un diccionario con la información del anime encontrado o None si no se encontró.
    """
    for index, row in df_anime.iterrows():
        if row["anime_id"] == id:
            return row
    return None


router = APIRouter()


@router.get("/anime/name/{anime_name}")
async def anime_name(anime_name: str):
    """
    Busca un anime por su nombre.

    Args:
    anime_name (str): El nombre del anime a buscar.

    Returns:
    dict: Un diccionario con la información del anime encontrado o un mensaje de error si no se encontró.
    """
    anime = search_anime(anime_name)
    print(anime)
    if anime is None:
        return {"error": "No se encontro el anime"}
    return {"anime": anime}


@router.get("/anime/id/{id}")
async def anime_id(id: int):
    """
    Busca un anime por su ID.

    Args:
        id (int): El ID del anime a buscar.

    Returns:
        dict: Un diccionario con la información del anime encontrado o un mensaje de error si no se encontró.
    """
    anime = search_anime_by_id(id)
    if anime is None:
        return {"error": "No se encontro el anime"}
    return {"anime": anime}


@router.get("/anime/genre/{genre}")
async def anime_genre(genre: str):
    """
    Retorna una lista de animes que pertenecen al genero especificado.

    Args:
    - genre (str): El genero del anime que se desea buscar.

    Returns:
    - dict: Un diccionario con la lista de animes que pertenecen al genero especificado.
    """
    # concidir el genre con el de la lista de generos
    genre_similares = get_close_matches(genre, lista_generos, cutoff=0.5)
    print(genre_similares)

    if not genre_similares:
        return {"error": "Genero no encontrado"}
    genre_similares = genre_similares[0]

    list_animes = []
    nodos = grafo.return_all_nodes()
    for nodo in range(len(nodos)):
        # Corregir la condición para verificar si el género buscado está presente en los géneros del anime
        anime_name = nodos[nodo]  # Obtener el nombre del anime del nodo
        if genre_similares in df_anime[df_anime["Name"] == anime_name]["Genres"].values:
            list_animes.append(
                df_anime[df_anime["Name"] == anime_name].iloc[0].to_dict()
            )

    print("canidad de animes encontrados -> ", len(list_animes))

    if not list_animes:
        return {"error": "No se encontraron animes"}

    return {"animes": list_animes}

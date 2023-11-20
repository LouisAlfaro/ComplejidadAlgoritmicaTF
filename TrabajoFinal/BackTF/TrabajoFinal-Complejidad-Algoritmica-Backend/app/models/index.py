from pydantic import BaseModel


class Graph(BaseModel):
    name: str
    nodes: str
    edges: int

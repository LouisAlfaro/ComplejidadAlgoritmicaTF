import pandas as pd
from typing import List, Tuple


class Grafo:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, origen, fin, peso):
        self.add_node(origen)
        self.add_node(fin)
        self.graph[origen][fin] = peso
        self.graph[fin][origen] = peso

    def return_all_nodes(self):
        return list(self.graph.keys())

    def print_graph(self):
        print("Grafo:")
        for indice_linea, node in enumerate(self.graph, start=1):
            print(indice_linea, node, self.graph[node])

    def export_to(self, filename):
        df = pd.DataFrame.from_dict(self.graph, orient="index").stack().reset_index()
        df.columns = ["Source", "Target", "Weight"]
        df.to_csv(filename, encoding="utf-8", index=False)

    def export_graph_to_dict(self):
        return self.graph

    def import_graph_from_file(self, file_path):
        """
        TODO: Cambiar el sistema para importar el grafo, cambiar a csv
        """
        self.graph = {}
        node_count = 0
        try:
            df = pd.read_csv(file_path)
            for index, row in df.iterrows():
                origen = row["Source"]
                fin = row["Target"]
                peso = row["Weight"]
                self.add_edge(origen, fin, float(peso))
                node_count += 1
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Error occurred:", str(e))

        return node_count

    def dijkstra_shortest_path(
        self, start: str, end: str
    ) -> Tuple[List[str], List[str]]:
        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0

        previous_nodes = {node: None for node in self.graph}

        unvisited_nodes = set(self.graph)

        visited_nodes = []

        while unvisited_nodes:
            current_node = min(unvisited_nodes, key=lambda node: distances[node])
            visited_nodes.append(current_node)

            if current_node == end:
                break

            unvisited_nodes.remove(current_node)

            for neighbor, weight in self.graph[current_node].items():
                distance = distances[current_node] + int(weight)

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node

        shortest_path = []
        current_node = end
        while previous_nodes[current_node] is not None:
            shortest_path.append(current_node)
            current_node = previous_nodes[current_node]
        shortest_path.append(start)
        shortest_path.reverse()

        return shortest_path, visited_nodes

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        edges = []
        for node in self.graph:
            for neighbor, weight in self.graph[node].items():
                edges.append((node, neighbor, weight))
        edges = sorted(edges, key=lambda item: item[2])  # Sort the edges list
        parent = {node: node for node in self.graph}
        rank = {node: 0 for node in self.graph}
        idx = 0
        while (
            e < len(self.graph) - 1 and i < len(edges) and idx <= 20
        ):  # Add a condition to check if i is within the range of edges
            u, v, w = edges[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append(u)
                result.append(v)
                self.union(parent, rank, x, y)
                idx += 1
        return result

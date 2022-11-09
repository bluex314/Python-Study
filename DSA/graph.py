class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = self.__create_graph_dict()

    def __create_graph_dict(self):
        graph_dict = {}
        for start, end in self.edges:
            if start in graph_dict:
                graph_dict[start].append(end)
            else:
                graph_dict[start] = [end]
        return graph_dict

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []

        for des in self.graph_dict[start]:
            if des not in path:
                new_paths = self.get_paths(des, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end):
        paths = self.get_paths(start, end)
        leng = len(paths[0])
        shortest_path = paths[0]
        for path in range(1, len(paths)):
            if leng > len(paths[path]):
                leng = len(paths[path])
                shortest_path = paths[path]
        return shortest_path


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]
    route_graph = Graph(routes)
    print(f"Graph dict: {route_graph.graph_dict}")

    start = "Mumbai"
    end = "New York"

    route_paths = route_graph.get_paths(start, end)
    print(f"Paths from {start} to {end} are: {route_paths}")
    print(f"Shortest Path from {start} {end}: {route_graph.get_shortest_path(start, end)}")
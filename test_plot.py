import networkx as nx

def bfs(G, start, end=None):
    queue = [(start, [start])]  # List of tuples containing current node and path
    visited = set()

    while queue:
        (node, path) = queue.pop(0)
        visited.add(node)

        # If the current node is the end node (if specified), return the path
        if end is not None and node == end:
            return path
        elif end is None and len(G[node]) == 0:
            return path
        else:
            # Add all unvisited adjacent nodes to the queue
            for adj in G[node]:
                if adj not in visited:
                    queue.append((adj, path + [adj]))

    return None  # If no path is found

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9), (5, 10)])
path = bfs(G, 1, 10)
print(path)

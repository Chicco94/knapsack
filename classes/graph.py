import matplotlib.pyplot as plt
import networkx as nx
from knapsack_element import KnapsackElement

class Graph(nx.DiGraph):
    def __init__(self, knapsack):
        super().__init__()
        self.knapsack = knapsack
        tot_nodes = len(self.knapsack)

        # Add all nodes to the graph
        nodes = range(1, tot_nodes+1)
        self.add_nodes_from(nodes)
        self.weighted_edges = []
        self.edge_labels = {}
        self.node_labels = {}
        # Add edges between all pairs of nodes
        for i in nodes:
            self.node_labels[i] = self.knapsack[i].get_value()
            for j in nodes:
                if i != j:
                    self.weighted_edges.append((i, j,self.knapsack[j].get_weight()))
                    self.edge_labels[(i,j)] = self.knapsack[j].get_weight()
                    
        # add one node for each node with an edge with its weight
        other_nodes = range(tot_nodes+1, tot_nodes*2+1)
        self.add_nodes_from(other_nodes)
        for i in other_nodes:
            self.node_labels[i] = 0
            self.weighted_edges.append((i, i-tot_nodes,self.knapsack[i-tot_nodes].get_weight()))
        
        self.add_weighted_edges_from(self.weighted_edges)


    def dfs(self, start):
        # Create a dictionary to store the visited nodes and their parent nodes
        visited = {start: None}

        # Define a recursive DFS function
        def dfs_util(node):
            # Visit all adjacent nodes
            for adj in self[node]:
                if adj not in visited:
                    visited[adj] = node
                    return dfs_util(adj)

        # Start the DFS at the start node
        dfs_util(start)

        # Highlight the final path
        path = [k for k in visited.keys()]
        edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        edge_colors = ['b' if e in edges else 'gray' for e in self.edges()]
        node_colors = ['b' if n in path else 'gray' for n in self.nodes()]
        self.show(node_colors,edge_colors) 


    def bfs(self, start:int,max_cost:int):

        # Define a recursive DFS function
        def bfs_util(G:Graph, start:int, visited:set, path:list,cost:int):
            visited.add(start)

            # Base case: if there are no more unvisited nodes, return the current path
            if len(visited) == len(G):
                return path

            # Recursive case: explore all unvisited adjacent nodes
            for adj in G[start]:
                if adj not in visited:
                    # Extend the current path and continue the search recursively
                    new_path = path + [adj]
                    result = bfs_util(G, adj, visited, new_path)
                    if result is not None:
                        return result

            return None  # If no path is found
        
        bfs_util(self,start,set(),[start],0)

    def show(self,node_colors='b',edge_colors='b'):
        '''plot the graph'''
        # Define the position of each node in the graph
        pos = nx.spring_layout(self)
        # Draw the nodes
        nx.draw_networkx_nodes(self, pos, node_color=node_colors, node_size=500)

        # Draw the curved edges
        nx.draw_networkx_edge_labels(self, pos, edge_labels=self.edge_labels, font_size=12, label_pos=0.5)
        nx.draw_networkx_edges(self, pos, width=2, alpha=0.5, edge_color=edge_colors, arrows=True, arrowsize=20, connectionstyle='arc3,rad=0.2')

        # Add labels to the nodes
        nx.draw_networkx_labels(self, pos, labels=self.node_labels, font_size=16)

        # Show the plot
        plt.axis('off')
        plt.show()



if __name__=="__main__":
    knapsack = {
        1:KnapsackElement(3,2),
        2:KnapsackElement(4,3),
        3:KnapsackElement(6,1),
        4:KnapsackElement(5,4)
    }
    g = Graph(knapsack)
    g.show()
    g.bfs(1+4)

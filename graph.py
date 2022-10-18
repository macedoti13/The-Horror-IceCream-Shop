class Graph:
    
    def __init__(self, nodes: list, directed: bool=True):
        """Creates a Graph object with an adjacency list.

        Args:
            nodes (list): list containing the name of the nodes. 
            directed (bool, optional): Indicates if the graph is of type directed. Defaults to True.
        """              
        # number of nodes definition
        self.nodes = nodes
        
        # type of graph definition
        self.directed = directed

        # adjacency list definition
        self.adj_list = {node: list() for node in range(len(self.nodes))}

    
    def add_edge(self, node1: str, node2: str):
        """Connects two nodes with an edge:
            - If graph is directed: node1 points to node2.
            - If graph is not directed: node1 points to node2 and node2 points to node1.


        Args:
            node1 (str): Name of the node1.
            node2 (str): Name of the node2.
        """        
        # edge from node1 to node2
        self.adj_list[node1].append(node2)

        # edge from node2 to node1 (only if not directed)
        if not self.directed:
            self.adj_list[node2].append(node1)

    
    def print_adj_list(self):
        """Prints the adjancency list."""
        for key in self.adj_list.keys():
            print(f"node {key}: {self.adj_list[key]}")
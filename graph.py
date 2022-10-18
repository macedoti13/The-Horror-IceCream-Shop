class Graph:
    
    def __init__(self, nodes: list, directed: bool=True):
        """Creates a Graph object.

        Args:
            nodes (list): list containing the name of the nodes. 
            directed (bool, optional): Indicates if the graph is of type directed. Defaults to True.
        """              
        # number of nodes definition
        self.nodes = nodes
        
        # type of graph definition
        self.directed = directed

        # adjacency list definition
        self.adj_list = {node: list() for node in range(self.nodes)}
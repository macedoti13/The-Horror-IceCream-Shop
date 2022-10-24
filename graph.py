class Graph:
    
    def __init__(self, nodes: list, directed: bool=True):
        """Creates a Graph object with an adjacency list.

        Args:
            nodes (list): list containing the name of the nodes. 
            directed (bool, optional): Indicates if the graph is of type directed. Defaults to True.
        """              
        # nodes in the graph
        self.nodes = nodes

        # number of nodes
        self.v = len(nodes)
        
        # type of graph definition
        self.directed = directed

        # adjacency list definition
        self.adj_list = {node: list() for node in nodes}

    
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


    def isReachable(self, s: str, d: str) -> bool:
        """Checks if a node d is reachable starting from another node s. 

        Args:
            s (str): node where the algorithm starts.
            d (str): node where the algorithm wants to end.

        Returns:
            bool: True if there is a path between from s to d, False otherwise.
        """        
        # creates visited and queue lists
        visited = []
        queue = []

        # adds source in visited and queue list
        queue.append(s)
        visited.append(s)

        # runs untill queue is empty
        while queue:

            # removes the first element from queue
            n = queue.pop(0)

            # if element is the destination, retunrs true
            if n == d:
                return True

            # if not, for every node that is connected to it and hasn't been visited, appends in the queue and mark it as visited
            for i in self.adj_list[n]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)

        # returns false if not path was founded
        return False


    def n_two_nodes_edges(self) -> int:   
        """Calculates the amount of combinations that can be made with two different connected nodes 
           in the graph. Uses bfs to check if there's a path between two nodes and sums 1 if it does.  


        Returns:
            int: Amount of connections.
        """        
        # open output file
        f = open('2FlavorCombinations.txt', 'w')

        # number of edges
        n_conncetions = 0 

        # for every source in the graph 
        for source in self.adj_list.keys():
            # for every destination in the graph
            for destination in self.adj_list.keys():
                # if destination is not the source
                if destination != source:
                    # if the destination in reachable from the source
                    if self.isReachable(source, destination):
                        # adds a new connection
                        n_conncetions += 1
                        # prints connection in the output file
                        f.write(f'{source} -> {destination}\n')

        f.close()

        return n_conncetions


    def n_three_nodes_edges(self) -> int:
        """Calculates the amount of combinations that can be made with three connected nodes 
           Uses bfs to check if there's a path between two nodes and if it does, checks how many 
           nodes can be reached by it. Presents the total number if the end. 

        Returns:
            int: amount of combinations.
        """        
        # creates new output file
        f = open('3FlavorCombinations.txt', 'w')

        # number of connections
        n_conncetions = 0

        # for each source in the graph
        for source in self.adj_list.keys():
            # for each destination in the graph 
            for destination in self.adj_list.keys():
                # if source is not the destination
                if destination != source:
                    # if the destination can be reached from the source 
                    if self.isReachable(source, destination):
                        # for each next_destination in the graph
                        for next_destination in self.adj_list.keys():
                            # if next_destination is not the source or the previous destination 
                            if next_destination not in [source, destination]:
                                # if the next destination can be reached from the previous destionation 
                                if self.isReachable(destination, next_destination):
                                    # writes in the output file
                                    f.write(f'{source} -> {destination} -> {next_destination}\n')
                                    # adds a new connections
                                    n_conncetions += 1

        # write number of combinations and closes the file
        f.write(f'\nTotal number of possible 3 flavors combinations: {n_conncetions}')
        f.close()

        return n_conncetions


def read_txt(file: str) -> Graph:
    """Reads a .txt file and creates a graph from it. The file must be in the 
       following format:

       "node_name -> node_name"

    Args:
        file (str): path of the file.

    Returns:
        Graph: graph created from the file.
    """    
    nodes = []
    edges = []

    with open(file) as f:
        # reading all lines in the file 
        lines = f.readlines()

        # iterates through each line, getting the nodes and the edges 
        for line in lines:
            content = line.split(' ')
            
            # adds first node in the nodes list (only if not already there)
            if content[0] not in nodes: 
                nodes.append(content[0])
            # adds second node in the nodes list (only if not already there)
            if content[2] not in nodes:
                nodes.append(content[2].split('\n')[0])
            
            # creates and edge for the nodes
            edges.append(tuple([content[0], content[2].split('\n')[0]]))
    
    # creates graph object with the nodes
    graph = Graph(nodes, directed=True)

    # creates the edges between the nodes 
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    return graph

import graph as g

def main():
    graph = g.read_txt('testfiles/casoleonardo20.txt')
    print(f'The number of possible combinations of two flavors is: {graph.n_two_nodes_edges()}')
    print(f'The number of possible combinations of three flavors is: {graph.n_three_nodes_edges()}')
    print('\nGraph:')
    graph.print_adj_list()

if __name__ == "__main__":
    main()
    
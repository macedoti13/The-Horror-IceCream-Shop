import graph as g

def main():
    graph = g.read_txt('test_files/casocohen60.txt')
    print(graph.n_two_nodes_edges())
    print(graph.n_three_nodes_edges())
    graph.print_adj_list()

if __name__ == "__main__":
    main()
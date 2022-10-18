import graph as g

def main():
    graph2 = g.read_txt('test_files/casocohen10.txt')
    print(graph2.n_two_nodes_edges())
    print(graph2.n_three_nodes_edges())

if __name__ == "__main__":
    main()
import graph as g

def main():
    graph = g.read_txt('testfiles/casocohen10.txt')
    #print(f'The number of possible combinations of two flavors is: {graph.n_two_nodes_edges()}')
    #print(f'The number of possible combinations of three flavores is: {graph.n_three_nodes_edges()}')
    #print('\nGraph:')
    #graph.print_adj_list()
    print(graph.isReachable('menta', 'abóbora'))

if __name__ == "__main__":
    main()
    
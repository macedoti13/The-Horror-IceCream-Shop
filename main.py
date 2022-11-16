import graph as g
from datetime import datetime

def main():
    inicio = datetime.now()
    graph = g.read_txt('testfiles/casoleonardo60.txt')
    print(f'The number of possible combinations of two flavors is: {graph.n_two_nodes_edges()}')
    print(f'The number of possible combinations of three flavors is: {graph.n_three_nodes_edges()}')
    print('\nGraph:')
    graph.print_adj_list()
    final = datetime.now()
    tempo = final - inicio
    print()
    print(f'tempo: {tempo}')

if __name__ == "__main__":
    main()
    
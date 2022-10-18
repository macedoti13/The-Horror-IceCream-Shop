import graph as g

def main():
    nodes = ["chocolate_branco", "graviola", "kiwi", "papaya_com_cassis", "maca_verde"]
    graph = g.Graph(nodes, directed=True)
    graph.add_edge("chocolate_branco", "papaya_com_cassis")
    graph.add_edge("chocolate_branco", "graviola")
    graph.add_edge("chocolate_branco", "kiwi")
    graph.add_edge("papaya_com_cassis", "maca_verde")
    graph.add_edge("papaya_com_cassis", "kiwi")
    graph.add_edge("graviola", "maca_verde")
    graph.add_edge("graviola", "kiwi")
    graph.print_adj_list()
    print(graph.n_two_nodes_edges())

if __name__ == "__main__":
    main()
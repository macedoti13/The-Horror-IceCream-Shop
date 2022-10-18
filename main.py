import graph as g

def main():
    nodes = ["chocolate_branco", "graviola", "kiwi", "papaya_com_cassis", "maca_verde"]
    graph = g.Graph(nodes, directed=True)
    graph.print_adj_list()
    graph.add_edge("chocolate_branco", "papaya_com_cassis")

if __name__ == "__main__":
    main()
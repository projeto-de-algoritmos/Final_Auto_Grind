import networkx as nx
import matplotlib.pyplot as plt
import random

def knapsack01(items, cap):
	tabela = [[0 for w in range(cap + 1)] for q in range(len(items) + 1)]
	
	for item in range(1, len(items) + 1):
		_, peso_item, valor_item = items[item-1]
		
		for aux_peso in range(1, cap + 1):
			if peso_item > aux_peso:
				tabela[item][aux_peso] = tabela[item-1][aux_peso]
			else:
				v1 = tabela[item-1][aux_peso-peso_item] + valor_item
				v2 = tabela[item-1][aux_peso]

				if v1 > v2:
					tabela[item][aux_peso] = v1
				else:
					tabela[item][aux_peso] = v2

	result = []
	cap_limite = cap

	for item in range(len(items), 0, -1):
		was_added = tabela[item][cap_limite] != tabela[item-1][cap_limite]

		if was_added:
			_, peso_item, _ = items[item-1]
			result.append(items[item-1])
			cap_limite -= peso_item
	
	return result

items = [
	("Túnica única", 2, 50), ("Espada de pau", 1, 20), ("Espada de fogo", 5, 70), ("Escudo de pedra", 9, 30),
	("Escudo de pau", 5, 20), ("Chapéu nobre", 7, 45), ("Machado de ferro", 3, 50), ("Bota de botas", 1, 40),
	("Queijo de mamute", 1, 10)
	]

mochila = []

G = nx.random_regular_graph(4, 7)

for (u, v) in G.edges():
    G.edges[u,v]['weight'] = random.randint(0,10)
    G.edges[u,v]['item'] = items[random.randint(0, len(items)-1)]

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)
nx.draw_networkx_labels(G, pos, font_size=16)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)
plt.show()

a = knapsack01(items, 15)
print(a)
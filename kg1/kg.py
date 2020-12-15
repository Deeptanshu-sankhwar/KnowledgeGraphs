import pandas as pd
import json
import networkx as nx
import matplotlib.pyplot as plt

f = open("../Scraper/faculty.json",)
dat = json.load(f)
f.close()

names = []
position = []
relation = []

size = len(dat)


for i in dat:
	names.append(i["name"])
	position.append(i["position"])
	relation.append("position")

kg1 = pd.DataFrame({'source':names, 'target':position, 'edge':relation})
print(kg1)

G = nx.from_pandas_edgelist(kg1,"source","target",edge_attr = True, create_using= nx.MultiDiGraph())

plt.figure(figsize = (40,40))
pos = nx.spring_layout(G, k = 0.5)
nx.draw(G, with_labels = True, node_color = 'red', edge_cmap = plt.cm.Blues, pos = pos)
plt.show()
print(names[3])
print(position[0])



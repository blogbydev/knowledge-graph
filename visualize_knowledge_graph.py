import networkx as nx
import matplotlib.pyplot as plt

def plot_knowledge_graph(entities, relationships):
  G = nx.DiGraph()
  for entity1, relationship, entity2 in relationships:
    G.add_edge(entity1, entity2, label=relationship)
  
  pos = nx.spring_layout(G)
  plt.figure(figsize=(8, 6))
  nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=5000, edge_color='black', font_size=10)
  edge_labels = {(entity1, entity2): relationship for entity1, relationship, entity2 in relationships}
  nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
  plt.show()
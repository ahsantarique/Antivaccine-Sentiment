
def random_get_stubborn_nodes(graph, PROB_STUBBORN):
  return np.random.permutation(graph.nodes)[:int(len(graph)*PROB_STUBBORN)]

def get_stubborn_nodes_by_degree(graph, PROB_STUBBORN):
  sorted_graph = sorted(graph.degree, key = lambda x: x[1], reverse=True)
  k = int(len(graph)*PROB_STUBBORN)

  stubborn = []
  for v,d in sorted_graph[:k]:
    stubborn.append(v)

  return stubborn

def get_stubborn_nodes_by_clustering_coef(graph, PROB_STUBBORN):
  import operator
  
  clus_coef = {}
  for node in graph.nodes():
      clus_coef[node] = nx.clustering(graph,node)

  sorted_graph= sorted(clus_coef.items(), key=operator.itemgetter(1),reverse=True)
  k = int(len(graph)*PROB_STUBBORN)

  stubborn = []
  for v,d in sorted_graph[:k]:
    stubborn.append(v)

  return stubborn

def get_stubborn_nodes_by_centrality(graph, PROB_STUBBORN):
  import operator
  
  centrality = nx.degree_centrality(graph)

  sorted_graph= sorted(centrality.items(), key=operator.itemgetter(1),reverse=True)
  k = int(len(graph)*PROB_STUBBORN)

  stubborn = []
  for v,d in sorted_graph[:k]:
    stubborn.append(v)

  return stubborn

def get_stubborn_nodes(graph, PROB_STUBBORN, STUBBORN_TYPE):
  if(STUBBORN_TYPE == "none"):
    stubborn = []
  elif (STUBBORN_TYPE == "random"):
    stubborn = random_get_stubborn_nodes(graph = graph, PROB_STUBBORN = PROB_STUBBORN)
  elif (STUBBORN_TYPE == "degree"):
    stubborn = get_stubborn_nodes_by_degree(graph = graph, PROB_STUBBORN= PROB_STUBBORN)
  elif (STUBBORN_TYPE == "cluster"):
    stubborn = get_stubborn_nodes_by_clustering_coef(graph = graph, PROB_STUBBORN = PROB_STUBBORN)
  elif (STUBBORN_TYPE == "centrality"):
    stubborn = get_stubborn_nodes_by_centrality(graph = graph, PROB_STUBBORN = PROB_STUBBORN)
  return stubborn
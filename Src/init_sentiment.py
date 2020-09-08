import numpy as np


def random_get_init_sentiments(graph, PROB_ANTI):

  PROB_PRO = 1-PROB_ANTI
  initial_sentiments = np.random.choice(2, len(graph), p=[PROB_PRO, PROB_ANTI])

  init_sentiments_dict = {i: initial_sentiments[j] for i,j in zip( list(graph.nodes) ,range(len(initial_sentiments)) )}
  # print(init_sentiments_dict)

  return init_sentiments_dict

def get_init_sentiments_by_degree(graph, PROB_ANTI):
  sorted_graph = sorted(graph.degree, key = lambda x: x[1], reverse=True)
  k = int(len(graph)*PROB_ANTI)

  init_sentiments_dict = {i: 0 for i in list(graph.nodes)}
  
  for v,d in sorted_graph[:k]:
    init_sentiments_dict[v] = 1

  return init_sentiments_dict

def get_init_sentiments_by_clustering_coef(graph, PROB_ANTI):  
  clus_coef = {}
  for node in graph.nodes():
      clus_coef[node] = nx.clustering(graph,node)

  sorted_graph= sorted(clus_coef.items(), key=operator.itemgetter(1),reverse=True)
  k = int(len(graph)*PROB_ANTI)

  init_sentiments_dict = {i: 0 for i in list(graph.nodes)}
  for v,d in sorted_graph[:k]:
    init_sentiments_dict[v] = 1

  return init_sentiments_dict


def get_init_sentiments_by_centrality(graph, PROB_ANTI):
  centrality = nx.degree_centrality(graph)

  sorted_graph= sorted(centrality.items(), key=operator.itemgetter(1),reverse=True)
  k = int(len(graph)*PROB_ANTI)

  init_sentiments_dict = {i: 0 for i in list(graph.nodes)}
  for v,d in sorted_graph[:k]:
    init_sentiments_dict[v] = 1

  return init_sentiments_dict


def get_init_sentiments(graph, PROB_ANTI, INIT): ##INIT = how you want to choose the anti-vaccine nodes initially
  if (INIT == "random"):
    init_sentiments_dict = random_get_init_sentiments(graph = graph, PROB_ANTI = PROB_ANTI)
  elif (INIT == "degree"):
    init_sentiments_dict = get_init_sentiments_by_degree(graph = graph, PROB_ANTI= PROB_ANTI)
  elif (INIT == "cluster"): ##clustering coefficient
    init_sentiments_dict = get_init_sentiments_by_clustering_coef(graph = graph, PROB_ANTI = PROB_ANTI)
  elif (INIT == "centrality"):
    init_sentiments_dict = get_init_sentiments_by_centrality(graph = graph, PROB_ANTI = PROB_ANTI)

  return init_sentiments_dict

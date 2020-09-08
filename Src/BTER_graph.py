# BTER graphs
import networkit as nk

def get_BTER_graph(filename):
	g = nx.read_edgelist(filename, create_using = nx.Graph(), nodetype=int)
	return g


if __name__ == '__main__':
	nnodes = g.numberOfNodes
	nedges = g.numberOfEdges
	nd = sorted([d for n, d in g.degree()], reverse=True)
	maxdegree = np.max(nd)

	print('nnodes: ', nnodes)
	print('nedges: ', nedges)
	print('maxdegree: ', maxdegree)
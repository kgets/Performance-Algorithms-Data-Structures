'''
For use in finding the shortest path from one node in a graph to the next.
Given a matrix g with nodes as rows and vertex weight between nodes as each column
Returns min distance to all nodes in graph
I could improve O(Time) even further with a priority queue.
'''
class Graph():
	def __init__(self, graph):
		self.V = len(graph)
		self.graph = graph

	def minDistance(self, dist, SPT):
		# Initilaize min distance as large int to represent ~INF
		min_ = 1e9
		# Search not nearest vertex not in Shortest Path Tree 
		for v in range(self.V):
			if dist[v] < min_ and not SPT[v]:
				min_ = dist[v]
				min_index = v
		return min_index

	# Dijkstra's single source graph algorithm 
	def dijkstra(self, sourceNode):
		dist = [1e9] * self.V
		dist[sourceNode] = 0
		SPT = [0] * self.V
		# loop size(v) times to find all vertecies
		for _ in range(self.V):
			# find closest vertex not in SPT 
			u = self.minDistance(dist, SPT)
			# mark vertex found (vertex in SPT)
			SPT[u] = 1
			# update distance values for adjacent verticies 
			# if (new distance to vertex is less and vertex not in SPT)
			for v in range(self.V):
				if self.graph[u][v] > 0 and not SPT[v] and dist[v] > dist[u] + self.graph[u][v]:
						dist[v] = dist[u] + self.graph[u][v]
		return dist



#test DJI
g = Graph([[-1, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, -1, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, -1, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, -1, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, -1, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, -1, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, -1, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, -1, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, -1]
		])
print(g.dijkstra(0))

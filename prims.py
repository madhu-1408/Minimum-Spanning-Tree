import networkx as nx
import matplotlib.pyplot as plt
import sys
import time
from time import sleep, time
#import clock

class MST:
	def __init__(self,vert):
		self.start = time()
		self.V= vert 
		self.graph = nx.Graph()
		
#adding edge
	def ad_edge(self,a,b,c):
		self.graph.add_edge(int(a), int(b), length= float(c))
#graph plotting
	def drawgraph(self):
		pos = nx.spring_layout(self.graph)
		nx.draw(self.graph, pos, with_labels = True)  
		edge_labels = nx.get_edge_attributes(self.graph,'length')
		nx.draw_networkx_edge_labels(self.graph, pos, edge_labels = edge_labels, font_size = 10) 
		return pos

	
	def minDistance(self, dist, mst):
		min = sys.maxsize
		for v in range(self.V):
			if dist[v] < min and mst[v] == False:
				min = dist[v]
				min_index = v
		return min_index

#prims algorithm
#main function
	def Prims(self):
		pos = self.drawgraph()
		distance = [] 
		parentnode = [None]* self.V 
		mst = [] 
		for i in range(self.V):
			distance.append(sys.maxsize)
			mst.append(False)
		distance[0] = 0
		parentnode[0]= -1
		for i in range(self.V):
			a = self.minDistance(distance, mst) 
			mst[a] = True
			for b in range(self.V):
				if (a, b) in self.graph.edges():
					
					if self.graph[a][b]['length'] > 0 and mst[b] == False and distance[b] > self.graph[a][b]['length']:
						distance[b] = self.graph[a][b]['length']
						parentnode[b] = a
		totSum = 0
		for i in range(self.V):
			if parentnode[i] != -1: 
				if (parentnode[i], i) in self.graph.edges():
					totSum += self.graph[parentnode[i]][i]['length']
					print(parentnode[i],end=" "+"to ")
					print(i,end=" "+"= ")
					print(self.graph[parentnode[i]][i]['length'])
					nx.draw_networkx_edges(self.graph, pos, edgelist = [(parentnode[i],i)], width = 2.5, alpha = 0.6, edge_color = 'r')
		
		self.end = time()
		RN=self.end - self.start
		print(f"running time={RN}")
		print("Total Weight ", totSum)
		plt.show()

if __name__ == "__main__":
    fo = open("sample.txt", 'r')
    file = fo.read().splitlines()
    fo.close()
    no = int(file[0])
    g = MST(no)
    for x in file[1:]:
        new = x.split()
        g.ad_edge(int(new[0]), int(new[1]), round(float(new[2]), 3))
		
    g.Prims()

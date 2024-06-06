import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import time
from time import sleep, time
#import clock

sns.set()

from collections import defaultdict

#represent a graph
class MST:

    def __init__(self,vertices):
        self.start = time()
        self.V= vertices 
        self.graph = [] 


    #adding edge
    def addedge(self,a,b,c):
        self.graph.append([a,b,c])

    # function to find an element i
    def find(self, p_node, i):
        if p_node[i] == i:
            return i
        return self.find(p_node, p_node[i])

    # to combine x and y sets
    def union(self, p_node, rank, x, y):
        xroot = self.find( p_node, x)
        yroot = self.find( p_node, y)

        if rank[xroot] < rank[yroot]:
             p_node[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
             p_node[yroot] = xroot
        else :
            p_node[yroot] = xroot
            rank[xroot] += 1

    # kruskals algorithm
    #main function
    def Kruskals(self):

        self.result =[] 
        i = 0 
        e = 0 
        self.graph =  sorted(self.graph,key=lambda item: item[2])
        p = [] ; pos = []

        for node in range(self.V):
            p.append(node)
            pos.append(0)

        while e < self.V -1 :

            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(p, u)
            y = self.find(p ,v)

            if x != y:
                e = e + 1
                self.result.append([u,v,w])
                self.union(p, pos, x, y)           
        G = nx.Graph()
        for u,v,weight  in self.graph:
            G.add_edge(u, v, length= float(weight))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels = True)  
        edge_labels = nx.get_edge_attributes(G, 'length')
        nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 5) 
        total_sum = 0
        for X in self.result:
            total_sum += X[2]
            if (X[0], X[1]) in G.edges():
                print(X[0]," to ",X[1]," = ",X[2])
                nx.draw_networkx_edges(G, pos, edgelist = [(X[0], X[1])], width = 2, alpha = 0.6, edge_color = 'r')

        self.end = time()
        print(f"running time={self.end - self.start}")
        print("Total Cost ", total_sum)
        plt.show()
    
if __name__ == "__main__":
    fo = open("sample.txt", 'r')
    file = fo.read().splitlines()
    fo.close()
    no = int(file[0])
    g = MST(no)
    for x in file[1:]:
        new = x.split()
        g.addedge(int(new[0]), int(new[1]), round(float(new[2]), 3))
    g.Kruskals()

"""
author: Sunil K B

description:
In Operating System, we come across the Resource Allocation Graph where each process and resources are considered to be vertices. 
Edges are drawn from resources to the allocated process, or from requesting process to the requested resource.
If this leads to any formation of a cycle then a deadlock will occur. 
Implement a Python application to check deadlock and display an appropriate message.

This is basically graph to detect a cycle

usage:
python3 DSA_3.py
"""

from collections import defaultdict
import re
import sys

if sys.version_info < (3, 0, 0):
	print(__file__ + ' requires Python 3, while Python ' + str(sys.version[0] + ' was detected. Terminating. Run - python3 ' + __file__))
	sys.exit(1)

# This class represents a undirected
# graph using adjacency list representation
class Graph:
	def __init__(self, vertices):

		# Store the number of verticies which is process plus resources
		self.V = vertices  # No. of vertices
		self.graph = defaultdict(list)

	# Function to add an edge to graph
	def add_edge(self, v, w):

		# Add graph edge on both side as its un-directed graph.
		self.graph[v].append(w)
		self.graph[w].append(v)

	# Recursively vist and mark the visited[] and parent to detect any cycle in sub-graph from vertice V
	def is_cycle_persent(self, v, visited, parent):
		# Mark the current node as visited
		visited[v] = True
		for i in self.graph[v]:

			# If the node is not visited then visit recursively sub-graph
			if visited[i] == False:
				if self.is_cycle_persent(i, visited, v):
					return True
			# If the adjacent vertice is visited and it is not parent of current vertice then there is a cycle in graph
			elif parent != i:
				return True
		return False

	def detect_cycle(self):
		visited = [False] * self.V
		for i in range(self.V):
			# Don't recur it is already visited
			if visited[i] is False:
				if (self.is_cycle_persent (i, visited, -1)) is True:
					return True
		return False

	# Print the graph
	def print_graph(self, resources):
		resources = int(resources)
		print("Resource Grpah stored Internally as: ")
		print(self.graph)
		print("\nMapping and Dependency between Resources and Processes\n")
		marked=dict()
		for x in self.graph:
			for y in self.graph[x]:
				if int(x) < resources and not "{}_{}".format(x, y) in marked:
					print("R{} <--> P{}".format(int(x) + 1, int(y) + 1 - resources))
				elif not "{}_{}".format(x, y) in marked:
					print("P{} <--> P{}".format(int(x) + 1 - resources, int(y) + 1 - resources))
				marked["{}_{}".format(x, y)] = 1
				marked["{}_{}".format(y, x)] = 1


# Main
if __name__ == '__main__':

	resources = ''
	while not re.match(r'^[0-9]+$', resources):
		resources = input('Enter Number of Resources: ')

	processes = ''
	while not re.match(r'^[0-9]+$', processes):
		processes = input('Enter Number of Processes: ')

	resources = int(resources)
	processes = int(processes)

	total_nodes = resources + processes
	print("Total Nodes in the graph is {}".format(total_nodes))
	g = Graph(total_nodes)

	for i in range(1, resources+1):
		for j in range(1, processes+1):
			connected = None
			while connected not in {'yes', 'no'}:
				connected = input("Is Resource R{} held by process P{} or P{} is waiting for R{} (yes/no): ".format(i, j, j, i))
				if connected == "yes":
					print("Adding Edge from {} <--> {}\n".format((i-1), (j - 1 + resources)))
					g.add_edge((i-1), (j - 1 +resources))

	for j in range(1, processes + 1):
		for k in range(j+1, processes + 1):
			connected = None
			while connected not in {'yes', 'no'}:
				connected = input("Is Process P{} waiting for process P{} or vice-versa (yes/no): ".format(j, k))
				if connected == "yes":
					print("Adding Edge from {} <--> {}\n".format((j - 1 + resources), (k - 1 + resources)))
					g.add_edge((j - 1 + resources), (k - 1 + resources))

	print ("--------------- Graph Connections----------------------------")
	g.print_graph(resources)
	print("--------------------------------------------------------------\n")

	print("\n************************************************************\n")
	if g.detect_cycle() == 1:
		print("Graph has a cycle. Deadlock Detected")
	else:
		print("Graph has no cycle. No Deadlock Detected.")
	print("\n************************************************************\n")
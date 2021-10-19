class Node:
	def __init__(self):
		self.fire = False # If fire is there in this node, turn self.fire = True
		self.DFS = False # If you explore this node using BFS, turn self.BFS = True
		self.BFS = False # If you explore this node using DFS, turn self.DFS = True
		self.dis = -1

class Holder:
	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y


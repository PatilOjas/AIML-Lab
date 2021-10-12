class Node:
	def __init__(self):
		self.fire = False # If fire is there in this node, turn self.fire = True
		self.DFS = False # If you explore this node using BFS, turn self.BFS = True
		self.BFS = False # If you explore this node using DFS, turn self.DFS = True

# grid = [[None for _ in range(10)] for _ in range(10)]

# for i in range(len(grid)):
# 	for j in range(len(grid)):
# 		grid[i][j] = Node()


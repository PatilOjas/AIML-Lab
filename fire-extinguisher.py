from tree import Node

grid_size_length = int(input("Enter number of rows in grid: "))
grid_size_breadth = int(input("Enter number of columns in grid: "))

grid = [[None for _ in range(grid_size_breadth)] for _ in range(grid_size_length)]

for i in range(grid_size_length):
	for j in range(grid_size_breadth):
		grid[i][j] = Node()

no_of_points = int(input("Enter number of points where fire has been detected: "))
print("Enter space separated co-ordinates of locations")

for i in range(no_of_points):
	point = tuple(map(int, input().split()))
	grid[point[0] - 1][point[1] - 1].fire = True


# doing BFS
def BFS():
	visited = [[False for _ in range(grid_size_length)] for _ in range(grid_size_breadth)]

	queue = []
	extinguisers_turned_on = []
	no_of_extinguishers = 0
	# FIFO -> first in first out

	for i in range(grid_size_length):
		for j in range(grid_size_breadth):
			if grid[i][j].fire == True:
				no_of_extinguishers += 1
				queue.append((i, j))

	dx = [0, 0, -1, 1, 1, -1, 1, -1]
	dy = [-1, 1, 0, 0, 1, 1, -1, -1]

	while len(queue) > 0:
		current = queue[0]
		queue.pop(0)
		x = current[0]
		y = current[1]
		visited[x][y] = 1
		for i in range(8):
			xx = x + dx[i]
			yy = y + dy[i]
			if xx < 0 or yy < 0 or xx >= grid_size_length or yy >= grid_size_breadth or grid[xx][yy] == False or visited[xx][yy]:
				continue 
			extinguisers_turned_on.append((xx + 1, yy + 1))
			# no_of_extinguishers += 1
	return extinguisers_turned_on

def DFS(stuck_coordinate):
	dx = [0, 1, 0, -1]
	dy = [-1, 0, 1, 0]

	stack = []
	stack.append([stuck_coordinate[0], stuck_coordinate[1]])

	vis = [[False for i in range(grid_size_breadth)] for j in range(grid_size_length)]
	
	while len(stack) > 0:
		current = stack[len(stack) - 1]
		stack.pop()

		x = current[0]
		y = current[1]


		if x < 0 or y < 0 or x >= grid_size_length or y >= grid_size_breadth or vis[x][y] == True or grid[x][y].fire == True:
			continue

		vis[x][y] = 1

		print((x + 1, y + 1), end=' -> ')

		if (x == 0 and y == 0) or (x == 0 and y == grid_size_breadth - 1) or (x == grid_size_length - 1 and y == 0) or (x == grid_size_length - 1 and y == grid_size_breadth - 1):
			return
		# time.sleep(1000)

		for i in range(4):
			xx = x + dx[i]
			yy = y + dy[i]
			stack.append([xx, yy])


extinguisers_turned_on = BFS()
print("System has turned on these co-ordinates: ")
for co_ordinate in extinguisers_turned_on:
	print(co_ordinate)

stuck_co_ordinate = tuple(map(int, input("Are you stuck? tell us your location: ").strip().split()))
stuck_co_ordinate = tuple((stuck_co_ordinate[0] - 1, stuck_co_ordinate[1] - 1))
DFS(stuck_co_ordinate)
import copy
from tree import *

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

grid_size_length = int(input("Enter number of rows in grid: "))
grid_size_breadth = int(input("Enter number of columns in grid: "))

grid = [[None for _ in range(grid_size_breadth)] for _ in range(grid_size_length)]

for i in range(grid_size_length):
	for j in range(grid_size_breadth):
		grid[i][j] = Node()

no_of_points = int(input("Enter number of points where fire has been detected: "))
print("Enter space separated co-ordinates of locations")

fire_point = []

for i in range(no_of_points):
	point = tuple(map(int, input().split()))
	fire_point.append(point)
	grid[point[0] - 1][point[1] - 1].fire = True

def printer():
	for i in grid:
		print(i)

def checkBound(x, y):
	if x >= 0 and y >= 0 and x < grid_size_length and y < grid_size_breadth and (grid[x][y]).fire == False:
		return True
	else:
		return False

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

def _BFS(x, y):
	found = False
	queue = []
	cur = Holder(x, y)
	(grid[cur.x][cur.y]).dis = 0
	queue.append(cur)
	while len(queue) > 0:
		cur = queue[0]
		queue.pop(0)
		if (cur.x == grid_size_length - 1) and (cur.y == grid_size_breadth - 1):
			found = True
			
		for i in range(4):
			nt = copy.deepcopy(cur)
			nt.x += dx[i]
			nt.y += dy[i]
			if checkBound(nt.x, nt.y) and grid[nt.x][nt.y].dis == -1:
				(grid[nt.x][nt.y]).dis = (grid[cur.x][cur.y]).dis + 1
				queue.append(nt)
	
	return found
	
path = []
ans = []
def DFS(stuck_co_ordinate, x, y, d):
	if x == stuck_co_ordinate[0] and y == stuck_co_ordinate[1]:
		onePath = list()
		onePath.append(tuple((grid_size_length - 1, grid_size_breadth - 1)))
		for i in range(d-1, -1, -1):
			onePath.append(ans[i])
		
		path.append(onePath)
		
		return
	
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if checkBound(nx, ny) and (grid[x][y]).dis - 1 == (grid[nx][ny]).dis:
			ans.append(tuple((nx, ny)))
			DFS(stuck_co_ordinate, nx, ny, d+1)
			ans.pop()


extinguisers_turned_on = BFS()
extinguisers_turned_on = set(fire_point + extinguisers_turned_on)
print("System has turned on these co-ordinates: ")
for co_ordinate in extinguisers_turned_on:
	print(co_ordinate)

stuck_co_ordinate = tuple(map(int, input("Are you stuck? tell us your location: ").strip().split()))
stuck_co_ordinate = tuple((stuck_co_ordinate[0] - 1, stuck_co_ordinate[1] - 1))
if not _BFS(stuck_co_ordinate[0], stuck_co_ordinate[1]):
	print("""Sorry to inform you that there is no path available from your position\n
# Please stay there until our fire extinguishers extinguish the fire and make a way for you\n
# It won't take long and keep yourself away from flames.""")
else:
	DFS(stuck_co_ordinate, grid_size_length - 1, grid_size_breadth - 1, 0)
	if len(path) > 0:
		print("Follow one of these paths")
		for i in path:
			i.append(i.pop(0))
			for j in i:
				print(f"({j[0] + 1},{j[1] + 1})", end=" -> ")
			print("\n")
# 	else:
# 		print("""Sorry to say that there is no path available from your position\n
# Please stay there until our fire extinguishers extinguish the fire and make a way for you\n
# It won't take long and keep yourself away from flames.""")
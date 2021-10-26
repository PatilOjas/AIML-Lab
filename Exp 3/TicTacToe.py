goalStates = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]

myBoard = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],
]

counterLimit = 5

def calculate_F_Value(i , j):
    maxElement = [-1, -1, -1]
    for _ in goalStates:
        empty = 0
        dot = 0
        cross = 0
        if (i, j) in _:
            for k in _:
                if myBoard[k[0]][k[1]] == '_':
                    empty += 1
                if myBoard[k[0]][k[1]] == 'o':
                    dot += 1
                if myBoard[k[0]][k[1]] == 'x':
                    cross += 1
        if maxElement[2] < cross:
            maxElement = [i, j, cross]
    
    return maxElement 
        

def playAI():
    fvalueList = []
    for i in range(3):
        for j in range(3):
            if myBoard[i][j] == '_':
                myBoard[i][j] = 'o'
                fvalueList.append(calculate_F_Value(i, j)) 
                myBoard[i][j] = '_'
    position = max(fvalueList, key=lambda x: x[2])
    myBoard[position[0]][position[1]] = 'o'

def checkWin():
    flagH = None
    counter = 0
    for i in range(3):
        for j in range(3):
            if myBoard[i][j] != '_':
                counter += 1 

    if counter == 9:
        flagH = "Draw"

    for location in goalStates:
        if myBoard[location[0][0]][location[0][1]] == 'x' and myBoard[location[1][0]][location[1][1]] == 'x' and myBoard[location[2][0]][location[2][1]] == 'x':
            flagH = True
            break
        elif myBoard[location[0][0]][location[0][1]] == 'o' and myBoard[location[1][0]][location[1][1]] == 'o' and myBoard[location[2][0]][location[2][1]] == 'o':
            flagH = False
            break
    return flagH

def printer():
    print(myBoard[0][0], "|", myBoard[0][1], "|", myBoard[0][2])
    print(myBoard[1][0], "|", myBoard[1][1], "|", myBoard[1][2])
    print(myBoard[2][0], "|", myBoard[2][1], "|", myBoard[2][2])
    print("\n\n")

   
endFlag = False

printer()

while True:
    humanLocation = list(map(int, input("Enter your next move location: ").strip().split()))
    humanLocation = [humanLocation[0] - 1, humanLocation[1] - 1]
    
    if myBoard[humanLocation[0]][humanLocation[1]] != '_':
        print("Watch oout!!\nIt's not an empty cell")
        continue

    myBoard[humanLocation[0]][humanLocation[1]] = 'x'
    printer()
    
    gameStatus = checkWin()
    if gameStatus == True:
        print("You won!!")
        endFlag = True
        break
    elif gameStatus == False:
        print("You lost!!")
        endFlag = True
        break
    elif gameStatus == "Draw":
        print("Match Draw!!")
        endFlag = True
        break
    
    if not endFlag: playAI()
    
    printer()

    gameStatus = checkWin()
    if gameStatus == True:
        print("You won!!")
        break
    elif gameStatus == False:
        print("You lost!!")
        break
    elif gameStatus == "Draw":
        print("Match Draw!!")
    

import queue
mazeTest = [['s',1,0, 0],
            [0,  1,0, 0],
            [0,  0,0, 0],
            [0,  1,0,'e']]
test = "U"
test1 = "DDDRRR"
start = (0,0)

#returns tuple of booleans where return[0] indicates validity
#and where return[1] indicates if its the end
def isValid(start,maze,moves):
    i,j = start
    for move in moves:
        if move == "U":
            i -= 1
        if move == "D":
            i += 1
        if move == "L":
            j -= 1
        if move == "R":
            j += 1

        if i >= len(maze) or i < 0 or j >= len(maze) or j < 0:
            return False,False
        elif maze[i][j] == 1:
            return False,False
        elif maze[i][j] == 'e':
            return True,True
    return True,False

def BFS(start,maze):
    q = queue.Queue()
    q.put("")
    curr = ""
    while not isValid(start,maze,curr)[1]:
        curr = q.get()
        [q.put(curr+i) for i in ["U","D","L","R"] if isValid(start,maze,curr+i)[0]]
    print("Shortest path to goal:",curr)

BFS(start,mazeTest)
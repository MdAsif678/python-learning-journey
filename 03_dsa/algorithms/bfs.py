# A ----- B
# |       |
# |       |
# C ----- D

graph = [
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]
]

# A --5-- B
# |       |
# 2       7
# |       |
# C --3-- D

graph2 = [
    [0,5,2,0],
    [5,0,0,7],
    [2,0,0,3],
    [0,7,3,0]
]

# A ----- B
# |       |
# |       |
# C ----- D
#  \     /
#    \ E
# Adjacency list



class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,num):
        self.queue.append(num)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, nothing to dequeue")
            return
        popped = self.queue.pop(0)
        return popped

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty, nothing to display")
            return
        return self.queue


graph3 = {
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D','E'],
    'D':['B','C','E'],
    'E':['C','D']
}

bfs = Queue()
bfs.enqueue('A')
visited = set()

while len(bfs.queue) != 0:
    element = bfs.dequeue()
    print(f"Visited {element}")
    visited.add(element)

    for neighbour in graph3[element]:
        if neighbour not in visited:
            bfs.enqueue(neighbour)
            visited.add(neighbour)


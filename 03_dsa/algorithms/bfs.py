# A ----- B
# |       |
# |       |
# C ----- D
#  \     /
#    \ E
# Adjacency list

# A ----- B
# |       |
# |       |
# C ----- D
#         |
#         E

# A ----- B
# |     / |
# |   /   |
# C ----- D
#  \     /
#    \ E

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, num):
        self.queue.append(num)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        popped = self.queue.pop(0)
        return popped

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return

        return self.queue


graph = {
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E"],
    "E":["C","D"]
}

bfs = Queue()
bfs.enqueue("C")
visited = set()

while len(bfs.queue) != 0:
    element = bfs.dequeue()
    print(f"Searched element {element}")
    visited.add(element)

    for neighbour in graph[element]:
        if neighbour not in visited:
            bfs.enqueue(neighbour)
            visited.add(neighbour)


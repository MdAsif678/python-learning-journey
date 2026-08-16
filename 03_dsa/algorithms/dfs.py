class Stack:
    def __init__(self):
        self.stack = []

    def push(self,num):
        self.stack.append(num)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Undeflow")
            return

        popped = self.stack.pop()
        return popped

    def display(self):
        if len(self.stack) == 0:
            print("Stack Undeflow")
            return

        for element in self.stack[::-1]:
            print(element)


    #     A
    #    / \
    #   B   C
    #  / \   \
    # D   E   F

graph = {
    "A":["B","C"],
    "B":["A","D","E"],
    "C":["A","F"],
    "D":["B"],
    "E":["B"],
    "F":["C"]
}
visited = set()

dfs = Stack()
dfs.push("A")

while len(dfs.stack) != 0:
    element = dfs.pop()
    print(f"Searched element {element}")
    visited.add(element)

    for neighbour in graph[element][::-1]:
        if neighbour not in visited:
            dfs.push(neighbour)
            visited.add(neighbour)


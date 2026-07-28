class PQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self,value,priority):
        self.queue.append((value,priority))

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return -1

        min_index = 0
        for i in range(len(self.queue)):
            if self.queue[i][1] < self.queue[min_index][1]:
                min_index = i 


        popped = self.queue.pop(min_index)
        return popped

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return -1

        min_index = 0
        for i in range(len(self.queue)):
            if self.queue[i][1] < self.queue[min_index][1]:
                min_index = i

        return f"Value: {self.queue[min_index][0]}\nPriority: {self.queue[min_index][1]}"

    def isempty(self):
        if len(self.queue) == 0:
            return True

        return False

    def display(self):
        if len(self.queue)  == 0:
            print("Queue is empty")
            return -1

        for values in self.queue:
            print(f"Value: {values[0]}, Priority: {values[1]}")
        print("="*100)

    

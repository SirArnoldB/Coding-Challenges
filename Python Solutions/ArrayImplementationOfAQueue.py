class MyQueue():
    def __init__(self, k) -> None:
        self.data = [0] * k 
        self.front = -1
        self.end = -1
        self.length = k

    def isEmpty(self):
        if self.front == -1 and self.end == -1:
            return True
        return False 

    def isFull(self):
        if (self.end + 1) % self.length == self.front:
            return True 
        return False 

    def enqueue(self, val):
        if self.isFull():
            return 
        elif self.isEmpty():
            front = end = 0
        else:
            self.end = (self.end + 1) % self.length 
        self.data.insert(self.end, val)

    def dequeue(self):
        if self.isEmpty():
            return 
        elif self.front == self.end:
            self.front = self.end = 0
        else:
            self.front = (self.front + 1) % self.length

# NB: If current position = i, next position = (i + 1) % k, 
# where k is the length of the array

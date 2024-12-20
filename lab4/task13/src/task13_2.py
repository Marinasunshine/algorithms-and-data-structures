class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, capacity=None):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.capacity is not None and self.size >= self.capacity

    def enqueue(self, data):
        if self.is_full():
            #print("Queue is full")
            return
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        #print(f"Added: {data}")

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return removed_data

    def display(self):
        current = self.head
        while current:
            #print(current.data, end=" ")
            current = current.next
        #print("None")


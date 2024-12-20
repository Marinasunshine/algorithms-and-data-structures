class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        data = self.top.data
        self.top = self.top.next
        return data

    def display(self):
        current = self.top
        while current:
            #print(current.data, end=" ")
            current = current.next
        #print("None")



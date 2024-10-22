class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def push(self, item):
        # Add an item to the top of the stack
        self.stack.append(item)

    def pop(self):
        # Remove and return the top item if the stack is not empty
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack") 

    def peek(self):
        # Return the top item without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None  # Return None if the stack is empty

    def size(self):
        # Return the number of items in the stack
        return len(self.stack)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop()) 

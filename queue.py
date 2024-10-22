class Queue:
    def __init__(self):
        # Initialize an empty list to hold the queue elements
        self.queue = []

    def is_empty(self):
        # Check if the queue is empty; return True if it is, False otherwise
        return len(self.queue) == 0

    def enqueue(self, item):
        # Add an item to the end of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        # Check if the queue is not empty before attempting to dequeue
        if not self.is_empty():
            return self.queue.pop(0)  # Remove and return the first item

    def size(self):
        # Return the number of items currently in the queue
        return len(self.queue)

# Example usage:
queue = Queue()  # Create an instance of the Queue class
queue.enqueue(1)  # Add 1 to the queue
queue.enqueue(2)  # Add 2 to the queue
queue.enqueue(3)  # Add 3 to the queue
print(queue.dequeue())  

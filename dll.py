# Define a class for the node of a doubly linked list
class DNode:
    def __init__(self, data):
        self.data = data  # The value the node stores
        self.next = None  # Pointer to the next node (initially None)
        self.prev = None  # Pointer to the previous node (initially None)


# Define the Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # The head node of the list, initially None

    # Method to insert a new node at the head (start of the list)
    def insert_at_head(self, data):
        new_node = DNode(data)  # Create a new node
        new_node.next = self.head  # New node's next will point to the current head
        if self.head:
            self.head.prev = new_node  # Set current head's prev to the new node
        self.head = new_node  # Update the head to point to the new node

    # Method to insert a new node at the tail (end of the list)
    def insert_at_tail(self, data):
        new_node = DNode(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Point the last node's next to the new node
        new_node.prev = current  # New node's prev points to the last node

    # Method to search for an element in the list
    def search(self, key):
        current = self.head
        while current:  # Traverse through the list
            if current.data == key:  # If the node's data matches the key
                return True
            current = current.next
        return False

    # Method to delete a node with a specific value
    def delete_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:  # If not the head node
                    current.prev.next = current.next
                else:  # If it's the head node
                    self.head = current.next
                if current.next:  # If not the tail node
                    current.next.prev = current.prev
                return True
            current = current.next
        return False  # Key not found

    # Method to display the linked list forward
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to display the linked list backward
    def display_backward(self):
        current = self.head
        if not current:
            return
        while current.next:  # Traverse to the tail
            current = current.next
        while current:  # Traverse backward from tail to head
            print(current.data, end=" -> ")
            current = current.prev
        print("None")


# Example usage of Doubly Linked List
dll = DoublyLinkedList()
dll.insert_at_head(3)
dll.insert_at_tail(7)
dll.insert_at_head(1)
dll.insert_at_tail(9)

print("Doubly Linked List (Forward):")
dll.display_forward()  # Output: 1 -> 3 -> 7 -> 9 -> None

print("Doubly Linked List (Backward):")
dll.display_backward()  # Output: 9 -> 7 -> 3 -> 1 -> None

# Searching for a value
print("Search for 7:", dll.search(7))  # Output: True


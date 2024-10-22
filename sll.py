# Define a class for the node of a singly linked list
class Node:
    def __init__(self, data):
        self.data = data  # The value the node stores
        self.next = None  # Pointer to the next node (initially None)


# Define the Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # The head node of the list, initially None

    # Method to insert a new node at the head (start of the list)
    def insert_at_head(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # New node's next will point to the current head
        self.head = new_node  # Update the head to point to the new node

    # Method to insert a new node at the tail (end of the list)
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Point the last node's next to the new node

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
        prev = None
        while current:
            if current.data == key:
                if prev:  # If it's not the head node
                    prev.next = current.next
                else:  # If it's the head node
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False  # Key not found

    # Method to display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage of Singly Linked List
sll = SinglyLinkedList()
sll.insert_at_head(3)
sll.insert_at_tail(7)
sll.insert_at_head(1)
sll.insert_at_tail(9)

print("Singly Linked List:")
sll.display()  # Output: 1 -> 3 -> 7 -> 9 -> None

# Searching for a value
print("Search for 7:", sll.search(7))  # Output: True

# Deleting a node
sll.delete_node(3)
print("After deleting 3:")
sll.display()  # Output: 1 -> 7 -> 9 -> None

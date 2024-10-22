# Class to represent a Node in the Binary Search Tree
class Node:
    def __init__(self, value):
        # Initialize a node with a given value and no children
        self.value = value  # The value/data of the node
        self.left = None    # Pointer to the left child (values smaller than this node)
        self.right = None   # Pointer to the right child (values larger than this node)

# Class to represent the Binary Search Tree itself
class BinarySearchTree:
    def __init__(self):
        # Initialize the Binary Search Tree with no root (empty tree)
        self.root = None

    # Method to insert a new value into the BST
    def insert(self, value):
        if self.root is None:
            # If the tree is empty, the new value becomes the root node
            self.root = Node(value)
        else:
            # Otherwise, use a helper method to insert the value recursively
            self._insert(value, self.root)

    # Helper method to insert a value starting from a given node
    def _insert(self, value, current_node):
        # If the new value is smaller than the current node's value
        if value < current_node.value:
            # Check if there is no left child, insert the new node here
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                # Otherwise, recurse to the left subtree
                self._insert(value, current_node.left)

        # If the new value is greater than the current node's value
        elif value > current_node.value:
            # Check if there is no right child, insert the new node here
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                # Otherwise, recurse to the right subtree
                self._insert(value, current_node.right)

    # Method to search for a value in the BST
    def search(self, value):
        # Start searching from the root node
        return self._search(value, self.root)

    # Helper method to search for a value starting from a given node
    def _search(self, value, current_node):
        # Base case: if we reach a None node, the value is not found
        if current_node is None:
            return False
        # If the value matches the current node's value, return True (found it)
        if value == current_node.value:
            return True
        # If the value is smaller than the current node's value, search in the left subtree
        elif value < current_node.value:
            return self._search(value, current_node.left)
        # If the value is greater, search in the right subtree
        else:
            return self._search(value, current_node.right)

    # Method to print the tree (in-order traversal)
    def in_order_traversal(self, node):
        if node:
            # First, recurse to the left subtree
            self.in_order_traversal(node.left)
            # Then, visit the current node
            print(node.value, end=" ")
            # Finally, recurse to the right subtree
            self.in_order_traversal(node.right)

# Example usage of the Binary Search Tree
if __name__ == "__main__":
    bst = BinarySearchTree()  # Create an empty Binary Search Tree

    # Insert values into the BST
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)

    # Search for some values
    print("Search for 7:", bst.search(7))  # Output: True
    print("Search for 21:", bst.search(21))  # Output: False

    # Print the tree using in-order traversal (should print values in ascending order)
    print("In-order traversal of BST: ", end="")
    bst.in_order_traversal(bst.root)  # Output: 2 5 7 10 12 15 20

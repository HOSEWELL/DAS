# Class to represent a Node in the Binary Tree
class Node:
    def __init__(self, value):
        # Initialize a node with a given value and no children
        self.value = value  # The value/data of the node
        self.left = None    # Pointer to the left child
        self.right = None   # Pointer to the right child

# Class to represent the Binary Tree itself
class BinaryTree:
    def __init__(self):
        # Initialize the Binary Tree with no root (empty tree)
        self.root = None

    # Method to insert a new value into the Binary Tree (level-order)
    def insert(self, value):
        new_node = Node(value)
        
        # If the tree is empty, the new node becomes the root
        if self.root is None:
            self.root = new_node
            return

        # Otherwise, do a level-order insertion using a queue
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)  # Dequeue the first node
            
            # If the left child is empty, insert the new node here
            if current_node.left is None:
                current_node.left = new_node
                return
            else:
                queue.append(current_node.left)

            # If the right child is empty, insert the new node here
            if current_node.right is None:
                current_node.right = new_node
                return
            else:
                queue.append(current_node.right)

    # Method to search for a value in the Binary Tree (uses level-order traversal)
    def search(self, value):
        if self.root is None:
            return False
        
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            # If the value is found, return True
            if current_node.value == value:
                return True
            
            # Continue searching in the left and right children
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        # If the value is not found, return False
        return False

    # Method for in-order traversal (left, root, right)
    def in_order_traversal(self, node):
        if node:
            # First, recurse to the left subtree
            self.in_order_traversal(node.left)
            # Visit the current node
            print(node.value, end=" ")
            # Finally, recurse to the right subtree
            self.in_order_traversal(node.right)

    # Method for pre-order traversal (root, left, right)
    def pre_order_traversal(self, node):
        if node:
            # Visit the current node
            print(node.value, end=" ")
            # Then, recurse to the left subtree
            self.pre_order_traversal(node.left)
            # Finally, recurse to the right subtree
            self.pre_order_traversal(node.right)

    # Method for post-order traversal (left, right, root)
    def post_order_traversal(self, node):
        if node:
            # First, recurse to the left subtree
            self.post_order_traversal(node.left)
            # Then, recurse to the right subtree
            self.post_order_traversal(node.right)
            # Visit the current node
            print(node.value, end=" ")

# Example usage of the Binary Tree
if __name__ == "__main__":
    bt = BinaryTree()  # Create an empty Binary Tree

    # Insert values into the Binary Tree (level-order insertion)
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)
    bt.insert(6)
    bt.insert(7)

    # Search for some values
    print("Search for 5:", bt.search(5))  # Output: True
    print("Search for 10:", bt.search(10))  # Output: False

    # Print the tree using in-order traversal
    print("\nIn-order traversal of Binary Tree: ", end="")
    bt.in_order_traversal(bt.root)  # Output: 4 2 5 1 6 3 7

    # Print the tree using pre-order traversal
    print("\nPre-order traversal of Binary Tree: ", end="")
    bt.pre_order_traversal(bt.root)  # Output: 1 2 4 5 3 6 7

    # Print the tree using post-order traversal
    print("\nPost-order traversal of Binary Tree: ", end="")
    bt.post_order_traversal(bt.root)  # Output: 4 5 2 6 7 3 1

# Print the left view of a binary tree
# Let's say we have a binary tree with the following structure:
#     8
#    /  \
#   5    9
#    \    \
#     6    13
#           \
#            15
# 
# The left view of the tree is:
# 8, 5, 6, 15
# 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        self.root.insert(data)

    def print_left_view(self, root, level):
        if root is None:
           return False

        if level == 1:
            print(root.data)
            return True
        
        left = self.print_left_view(root.left, level - 1)
        if not left:
            right = self.print_left_view(root.right, level - 1)

        return True if left or right else False
    
    def left_view(self):
        level = 1
        
        while self.print_left_view(self.root, level):
            level += 1


tree = BinaryTree(8)
tree.insert(5)
tree.insert(9)
tree.insert(6)
tree.insert(13)
tree.insert(15)
tree.left_view()

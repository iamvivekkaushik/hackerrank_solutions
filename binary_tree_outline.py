# Print the left view of a binary tree
# Let's say we have a binary tree with the following structure:
#     8
#    /  \
#   5    9
#  /  \    \
# 4     6    13
# 
# The left view of the tree is:
# 8, 5, 4, 9, 13
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
            return root.data
        
        left = self.print_left_view(root.left, level - 1)
        if not left:
            right = self.print_left_view(root.right, level - 1)

        return left or right

    def print_right_view(self, root, level):
        if root is None:
           return False

        if level == 1:
            return root.data
        
        right = self.print_right_view(root.right, level - 1)
        if not right:
            left = self.print_right_view(root.left, level - 1)

        return right or left

    def left_view(self):
        level = 1
        left = []

        while True:
            value = self.print_left_view(self.root, level)
            if value == False:
                break

            if isinstance(value, int):
                left.append(value)
            level += 1

        return left

    def right_view(self):
        level = 1
        right = []

        while True:
            value = self.print_right_view(self.root, level)
            if value == False:
                break

            if isinstance(value, int):
                right.append(value)

            level += 1

        return right

    
    def print_outline(self):
        left = self.left_view()
        right = self.right_view()
        
        # create set of left and right
        outline_values = set(left + right)

        for i in outline_values:
            print(i)
    


tree = BinaryTree(8)
tree.insert(5)
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(13)
tree.print_outline()

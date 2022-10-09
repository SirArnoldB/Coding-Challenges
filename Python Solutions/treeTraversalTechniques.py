class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

# Pre-Order Traversal
# Root - Left Node - Right Node
pre_order_traversal_res = []


def pre_order_traversal(root):
    if root:
        pre_order_traversal_res.append(root.data)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


pre_order_traversal(n1)
print(pre_order_traversal_res)

# Post-Order Traversal
# Left Node - Right Node - Root
post_order_traversal_res = []


def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        post_order_traversal_res.append(root.data)


post_order_traversal(n1)
print(post_order_traversal_res)

# In-Order Traversal
# Left Node - Root - Right Node
in_order_traversal_res = []


def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        in_order_traversal_res.append(root.data)
        in_order_traversal(root.right)


in_order_traversal(n1)
print(in_order_traversal_res)

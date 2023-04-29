# Given a binary tree, write a serialize function that converts the tree into a string and
# a deserialize function that converts a string to a binary tree.
# You may serialize the tree into any string representation you want as long as it can be deseralized.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    res = []

    def dfs(root):
        if not root:
            res.append("x")
            return
        res.append(root.val)
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return "->".join(res)


def deserialize(nodes_string):
    def dfs(nodes):
        val = next(nodes)
        if val == "->":
            return
        curr = Node(int(val))
        curr.left = dfs(nodes)
        curr.right = dfs(nodes)

        return curr

    # create an iterator that returns a token each time we call 'next'
    return dfs(iter(nodes_string.split("->")))

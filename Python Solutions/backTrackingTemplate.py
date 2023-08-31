"""
# How to implement a backtracking algorithm

    ### Draw the tree, draw the tree, draw the tree!!!

Draw a state-space tree to visualize the problem. A small test case that's big enough to reach at least one solution (leaf node). 
This is super important! 
Once you draw the tree, the rest of the work becomes so much easier - simply traverse the tree depth-first.

When drawing the tree, bear in mind:

# 1. how do we know if we have reached a solution?
# 2. how do we branch (generate possible children)?

def dfs(start_index, path):
    if is_leaf(start_index):
        report(path)
        return 
    for edge in get_edges(start_index):
        path.add(edge)
        dfs(start_index + 1, path)
        path.pop()

# start_index is used to keep track of the current level of the state-space tree we are in.

# edge is the choice we make; the string a, b in the above state-space trees.

# The main logic we have to fill out are

    # is_leaf
    # get_edges
    
# Template v1.1

def dfs(start_index, path):
    if is_leaf(start_index):
        report(path)
        return
    for edge in get_edges(start_index):
        # prune if needed
        if not is_valid(edge):
            continue
        path.add(edge)
        # increment start_index
        dfs(start_index + len(edge), path)
        path.pop()

# The differences are
    # Added pruning step that checks if a branch is valid using is_valid
    # Increment start_index by a variable size instead of always 1

# Backtracking 1 Template Final Form

# this template is typically used to answer question such as
# find **all** the combination of ...
# generate **all** valid...

ans = []
def dfs(start_index, path, [...additional states]):
    if is_leaf(start_index):
        ans.append(path[:]) # add a copy of the path to the result
        return
    for edge in get_edges(start_index, [...additional states]):
        # prune if needed
        if not is_valid(edge):
            continue
        path.add(edge)
        if additional states:
            update(...additional states)
        dfs(start_index + len(edge), path, [...additional states])
        # revert(...additional states) if necessary e.g. permutations
        path.pop()

"""

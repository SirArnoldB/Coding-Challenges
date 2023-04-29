# Write code to remove duplicates from an unsorted linked list
# Follow up: how would you solve this problem if a temporary buffer is not allowed?
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicates(listNode: ListNode):
    curr_node = listNode
    seen_nodes = set()

    while curr_node:
        next_node = curr_node.next
        if next_node in seen_nodes:
            curr_node.next = next_node.next
        else:
            seen_nodes.append(curr_node)
            curr_node = curr_node.next
    return listNode

# Follow up - No buffer allowed
# Iterate with two pointers 
    # current - iterates through the linked list
    # runner - checks all subsequent nodes for duplicates
def removeDups(listNode : ListNode):
    curr_node = listNode
    while curr_node:
        # remove all future nodes that have the same value
        runner = curr_node
        while runner.next:
            if runner.next.val == curr_node.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr_node = curr_node.next 


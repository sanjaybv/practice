class Node:
    def __init__(self, value=None, num_children=2):
        self.left, self.right, self.parent  = None, None, None
        self.value = value
        self.visited = False

def bst_from_array(array, parent=None):
    if not array:
        return None
    value, index = array[len(array)/2], len(array)/2
    cur_node = Node(value)
    cur_node.left = bst_from_array(array[:index], cur_node)
    cur_node.right = bst_from_array(array[index+1:], cur_node)
    cur_node.parent = parent
    return cur_node

def preorder(root):
    if not root:
        return
    left = root.left
    right = root.right
    print root.value, left.value if left else None, right.value if right else None
    preorder(root.left)
    preorder(root.right)

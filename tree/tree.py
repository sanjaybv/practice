from stack import Stack

class Node:
    def __init__(self, value=None, num_children=2):
        self.children = [None] * num_children
        self.value = value
        self.visited = False

def bst_from_array(array):
    if not len(array):
        return None
    value, index = array[len(array)/2], len(array)/2
    cur_node = Node(value)
    cur_node.children[0] = bst_from_array(array[:index])
    cur_node.children[1] = bst_from_array(array[index+1:])
    return cur_node

def make_tree():
    root = Node(1)
    root.children[0] = Node(2)
    root.children[1] = Node(3)
    root.children[0].children[0] = Node(4)
    root.children[0].children[1] = Node(5)
    root.children[0].children[1].children[0] = Node(6)

    return root

def traverse_inorder(root):
    if not root:
        return
    traverse_inorder(root.children[0])
    print root.value,
    traverse_inorder(root.children[1])

def traverse_preorder(root):
    if not root:
        return
    print root.value,
    traverse_preorder(root.children[0])
    traverse_preorder(root.children[1])

def traverse_postorder(root):
    if not root:
        return
    traverse_postorder(root.children[0])
    traverse_postorder(root.children[1])
    print root.value,

def traverse_nonrecursive(root):
    s = Stack()
    s.push(root)
    while len(s):
        cur_node = s.pop()
        if not cur_node:
            continue
        print cur_node.value,
        s.push(cur_node.children[1])
        s.push(cur_node.children[0])

def is_balanced(root):

    if not root:
        return True, 1

    left_isb, left_depth = is_balanced(root.children[0])
    right_isb, right_depth = is_balanced(root.children[1])

    if not left_isb or not right_isb:
        return False, 0
    else:
        if abs(left_depth - right_depth) > 1:
            return False, 0
        else:
            return True, max(left_depth, right_depth) + 1

if __name__ == '__main__':
    root = make_tree()
    root = bst_from_array(range(1, 6))

    traverse_inorder(root)
    print 
    traverse_preorder(root)
    print 
    traverse_postorder(root)
    print
    traverse_nonrecursive(root)
    print
    print is_balanced(root)

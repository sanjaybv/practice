from stack import Stack
from collections import deque

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

def make_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(6)

    return root

def traverse_inorder(root):
    if not root:
        return
    traverse_inorder(root.left)
    print root.value,
    traverse_inorder(root.right)

def traverse_preorder(root):
    if not root:
        return
    left = root.left
    right = root.right
    print root.value, left.value if left else None, right.value if right else None
    traverse_preorder(root.left)
    traverse_preorder(root.right)

def traverse_postorder(root):
    if not root:
        return
    traverse_postorder(root.left)
    traverse_postorder(root.right)
    print root.value,

def iterative_preorder(root):
    stack = deque()
    stack.append(root)
    while stack:
        node = stack.pop()
        if not node:
            continue
        print node.value,
        stack.append(node.right)
        stack.append(node.left)

def stack_lefts(stack, node):
    while node:
        stack.append(node)
        node = node.left

def iterative_inorder(root):
    stack = deque()
    stack_lefts(stack, root)
    while stack:
        elem = stack.pop()
        print elem.value,
        stack_lefts(stack, elem.right)

def iterative_postorder(root):
    stack = deque()
    stack_lefts(stack, root)
    while stack:
        elem = stack.pop()
        print elem.value,
        if stack and stack[-1].right != elem:
            stack_lefts(stack, stack[-1].right)
    

def is_balanced(root):

    if not root:
        return True, 1

    left_isb, left_depth = is_balanced(root.left)
    right_isb, right_depth = is_balanced(root.right)

    if not left_isb or not right_isb:
        return False, 0
    if abs(left_depth - right_depth) > 1:
        return False, 0
    return True, max(left_depth, right_depth) + 1

if __name__ == '__main__':
    root = make_tree()
    root = bst_from_array([0, 1, 4, 6, 7, 8, 10, 12, 18])

    print 'rec pre'
    traverse_preorder(root)
    print
    print 'it pre'
    iterative_preorder(root)
    print
    print 'rec in'
    traverse_inorder(root)
    print
    print 'it in'
    iterative_inorder(root)
    print
    print 'rec post'
    traverse_postorder(root)
    print
    print 'it post'
    iterative_postorder(root)
    print
    print is_balanced(root)

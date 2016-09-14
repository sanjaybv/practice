class Node:
    def __init__(self, value=None, num_children=2):
        self.children = [None] * num_children
        self.value = value
        self.visited = False

def make_tree():
    root = Node(1)
    root.children[0] = Node(2)
    root.children[1] = Node(3)
    root.children[0].children[0] = Node(4)
    root.children[0].children[1] = Node(5)

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

if __name__ == '__main__':
    root = make_tree()

    traverse_inorder(root)
    print 
    traverse_preorder(root)
    print 
    traverse_postorder(root)

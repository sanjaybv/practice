import tree
import sys

def next_inorder(node):
    # error check
    if not node:
        return None

    # check for right child's left most
    if node.right:
        return leftmost(node.right)

    # parent of a left child
    parent = node.parent
    while parent:
        if parent.right != node:
            return parent
        node = parent
        parent = node.parent
    return None

def first_inorder(root):
    return leftmost(root)

def leftmost(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root

def main():
    root = tree.bst_from_array([4, 2, 5, 1, 6, 3, 7])
    tree.preorder(root)

    node = first_inorder(root)
    while node:
        print node.value,
        node = next_inorder(node)

    

if __name__ == '__main__':
    main()

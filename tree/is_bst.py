import tree
import sys

def is_bst(root):
    return is_bst_recurse(root, -sys.maxint-1, sys.maxint)

def is_bst_recurse(node, range_min, range_max):
    if not node:
        return True
    if not range_min <= node.value <= range_max:
        return False
    return is_bst_recurse(node.left,
                          range_min,
                          node.value-1) \
        and is_bst_recurse(node.right,
                           node.value,
                           range_max)


def main():
    root = tree.bst_from_array(range(10))
    root2 = tree.bst_from_array([0, 1, 4, 4, 6, 7, 8, 10, 12, 18])
    tree.traverse_preorder(root)
    print 'is_bst:', is_bst(root2)
    

if __name__ == '__main__':
    main()

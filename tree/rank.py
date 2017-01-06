from tree import Node, preorder

class TreeRank(object):
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = Node([data, 0])
            return

        it_node = self.root
        cur_rank = 0
        while True:
            if data < it_node.value[0]:
                it_node.value[1] += 1
                if not it_node.left:
                    it_node.left = Node([data, it_node.value[1] - 1])
                    return
                else:
                    it_node = it_node.left
            else:
                if not it_node.right:
                    it_node.right = Node([data, it_node.value[1] + 1])
                    return
                else:
                    it_node = it_node.right

    def track(self, elem, root):
        if not root:
            return None
        if elem == root.value[0]:
            return root.value[1]
        elif elem < root.value[1]:
            return self.track(elem, root.left)
        return self.track(elem, root.right)

if __name__ == '__main__':
    tree = TreeRank()
    for x in [1, 6, 4, 3, 8, 9, 2, 7]:
        tree.add(x)
        preorder(tree.root)
        print tree.track(4, tree.root)

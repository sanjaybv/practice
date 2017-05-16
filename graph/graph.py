from queue import Queue
from stack import Stack
from collections import defaultdict

class Graph(object):
    def __init__(self):
        self._graph = defaultdict(set)

    def add_edge(self, from_node, to_node):
        self._graph[from_node].add(to_node)

    def adjacent(self, node):
        return self._graph.get(node)

graph = {
        'A' : ['B', 'C', 'D'],
        'B' : ['E'],
        'C' : ['B'],
        'D' : [],
        'E' : ['F'],
        'F' : []
        }

def main():
    visited = set()

    # BFS - Queue ; DFS - Stack

    q = Stack() #Queue()
    q.push('D')
    visited.add('D')
    while len(q):
        cur_node = q.pop()
        if cur_node == 'F':
            print 'YES'
            break
        for node in graph[cur_node]:
            if node not in visited:
                q.push(node)
                visited.add(node)
    else:
        print 'NO'


if __name__ == '__main__':
    main()

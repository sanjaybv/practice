from queue import Queue
from stack import Stack

def main():
    graph = {
            'A' : ['B', 'C', 'D'],
            'B' : ['E'],
            'C' : ['B'],
            'D' : [],
            'E' : ['F'],
            'F' : []
            }
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

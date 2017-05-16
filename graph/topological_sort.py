# Topological Sort Ordering
graph = {
        'A' : ['B', 'C', 'D'],
        'B' : ['E'],
        'C' : ['B'],
        'D' : [],
        'E' : ['F'],
        'F' : []
        }

def top_sort(graph):
    stack = []
    visited = set()

    for node in graph:
        print 
        to_rec(stack, visited, node, graph)

    print stack

def to_rec(stack, visited, node, graph):
    print node
    if node in visited:
        return

    visited.add(node)

    for adj_node in graph[node]:
        to_rec(stack, visited, adj_node, graph)

    stack.append(node)

def main():
    top_sort(graph)

if __name__ == '__main__':
    main()

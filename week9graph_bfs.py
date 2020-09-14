'''ISCG6426 Week 9 graphs
Daniel E'''
G = {
    'A': ['C', 'D', 'B'],
    'B': ['C'],
    'C': ['D', 'A'],
    'D': ['A'],
    'E': ['B'],
    'F': ['D', 'F']
}

G2 = {
    'X': [],
    'Y': ['Z'],
    'Z': ['Y', 'Z']
}
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.insert(0, item)

    def pop(self):
        return self.queue.pop()

    def __str__(self):
        return f'Queue: {self.queue}'



def BFS(graph, start_node, destination):
    visited = set()
    queue = Queue()
    queue.push(start_node)
    #v = queue.pop()

    while len(queue.queue) != 0:
        v = queue.pop()
        if v == destination:
            print("wow v made it")
            print(visited)
            return destination
        print(f'graph[{v}]: {graph[v]}')
        for neighbour in graph[v]:
            if neighbour not in visited:
                queue.push(neighbour)
                print(f'Added {neighbour} to queue')
            else:
                print(f'Already visited neighbour: {neighbour}')
        visited.add(v)
        print(f'queue is: {queue} - visited is {visited}')
    print('did not find')
    return -1


#BFS(G, 'E', 'D')
BFS(G2, 'Y', 'X')
'''ISCG6426 Week 9 graphs
Daniel E'''
G = {
    'A': ['C', 'D', 'B'],
    'B': ['C'],
    'C': ['D'],
    'D': ['A'],
    'E': [],
    'F': ['D', 'F']
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



def BFS(graph, start_node):
    visited = set()
    queue = Queue()
    queue.push(start_node)
    #v = queue.pop()

    while len(queue.queue) != 0:
        v = queue.pop()
        print(f'graph[{v}]: {graph[v]}')
        for neighbour in graph[v]:
            if neighbour not in visited:
                queue.push(neighbour)
                print(f'Added {neighbour} to queue')
            else:
                print(f'Already visited neighbour: {neighbour}')
        visited.add(v)
        print(f'queue is: {queue} - visited is {visited}')


BFS(G, 'A')

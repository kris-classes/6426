class TommyQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return f'Queue: {self.queue}'

    def push(self, item):
        self.queue.insert(0, item)

    def pop(self):
        return self.queue.pop()

if __name__ == '__main__':
    q = TommyQueue()
    q.push('dog')
    q.push('puppy')
    print(q)
    print(q.pop())
    print(q.pop())
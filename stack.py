class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f'Stack: {self.stack}'

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

s = Stack()
s.push('cat')
s.push('lorax')
s.push('Lynx')
# recent_item = s.pop()
# print(recent_item)
print(s)
print(s.pop())
print(s.pop())
print(s.pop())

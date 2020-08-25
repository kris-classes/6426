import sys

sys.setrecursionlimit(100)
class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous
        self.visited = False

    def __str__(self):
        return f'{self.data}'
        #return f'{self.previous} <-- {self.data} --> {self.next}'


node_22 = Node(22)
node_2 = Node(2)
node_77 = Node(77)
node_6 = Node(6)


node_22.next = node_2
node_2.next = node_77
node_77.next = node_6
node_6.next = node_22

node_2.previous = node_22
node_77.previous = node_2
node_6.previous = node_77
node_22.previous = node_6



'''def print_linked_list(node, direction = 'right'):
    current_node = node
    if direction == 'right':
        while current_node.next != node:
            print(f'Current node = {current_node} , object at {hex(id(current_node))}')
            current_node = current_node.next
    else:
        while current_node.previous != node:
            print(f'Current node = {current_node} , object at {hex(id(current_node))}')
            current_node = current_node.previous

    print(f'Current node = {current_node} , object at {hex(id(current_node))}')
    print(" ")'''

'''def print_linked_list(node, direction = 'right'):
    current_node = node
    if direction == 'right':
        while current_node.visited != True:
            print(f'Current node = {current_node} , object at {hex(id(current_node))}')
            current_node.visited = True
            current_node = current_node.next
    else:
        while current_node.visited != True:
            print(f'Current node = {current_node} , object at {hex(id(current_node))}')
            current_node.visited = True
            current_node = current_node.previous'''

def print_linked_list(node, direction = 'right'):
    visited = set()
    current_node = node
    if direction == 'right':
        while current_node not in visited:
            visited.add(current_node)
            print(f'Current node = {current_node} , object at {hex(id(current_node))}')
            current_node = current_node.next
    else:
        while current_node not in visited:
            visited.add(current_node)
            print(f'Current node = {current_node} , object at {hex(id(current_node))}')
            current_node = current_node.previous

    #print(f'Current node = {current_node} , object at {hex(id(current_node))}')
    print(" ")

if __name__ == '__main__':
    print_linked_list(node_77, 'left')



'''def insert_node(new_node, position):
    # print(f'make position {position} point to {new_node}')
    # we want to point new node to next node '43'
    new_node.next = position.next
    # print(f'{new_node} points to: {position.next}')
    # point previous node to new node
    position.next = new_node

def delete_node(previous_node):
    # save reference to 13
    junk_node = previous_node.next
    # change what 6 points to (43)
    previous_node.next = junk_node.next
    # delete 13
    del junk_node'''

class TreeNode:
    def __init__(self, root, nodes=None):
        self.root = root
        self.nodes = nodes




'''node_13 = Node(13)
insert_node(node_13, node_6)

print_linked_list(node_22)

delete_node(node_6)
print_linked_list(node_22)'''

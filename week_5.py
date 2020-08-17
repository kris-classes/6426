
class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __str__(self):
        if self.next is not None:
            return f'{self.data} --> {self.next.data}'
            # return f'{self.data}'
        else:
            return f'{self.data} --> nothing'


class TreeNode:
    def __init__(self, data, nodes=None):
        self.data = data
        self.nodes = nodes




node_22 = Node(22)
node_2 = Node(2)
node_77 = Node(77)
node_6 = Node(6)
node_43 = Node(43)
node_76 = Node(76)
node_89 = Node(89)

node_22.next = node_2
node_2.next = node_77
node_77.next = node_6
node_6.next = node_43
node_43.next = node_76
node_76.next = node_89


def print_linked_list(node):
    current_node = node
    while current_node.next != None:
        print(current_node)
        current_node = current_node.next
    print(" ")


def insert_node(new_node, position):
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
    del junk_node



print_linked_list(node_22)


node_13 = Node(13)
insert_node(node_13, node_6)

print_linked_list(node_22)

delete_node(node_6)
print_linked_list(node_22)

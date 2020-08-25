


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        #self.nodes = nodes
    def __str__(self):
        pass



node_3 = Node(3)
node_8 = Node(8)
node_5 = Node(5)
node_4 = Node(4)
node_2 = Node(2)
node_1 = Node(1)
node_0 = Node(0)
node_6 = Node(6)
node_10 = Node(10)
node_7 = Node(7)
node_9 = Node(9)

node_5.right = node_8
node_5.left = node_3
node_3.right = node_4
node_3.left = node_2
node_2.left = node_1
node_1.left = node_0
node_8.right = node_10
node_8.left = node_6
node_6.right = node_7
node_10.left = node_9


def search(node, value):
    print(f'Current node is {node.data}')
    if node.data == value:
        print("found")
        return node
    elif value < node.data:
        print('going left')
        search(node.left, value)
    else:
        print('going right')
        search(node.right, value)



search(node_5, 4)

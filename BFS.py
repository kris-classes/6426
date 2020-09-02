import tommy_queue as Queue

# Defining the node of ternary search tree
class Node:
    def __init__(self, data, left=None, mid=None, right=None):
        self.data = data
        self.left = left
        self.mid = mid
        self.right = right

# __str__ for the user to display the data
    def __str__(self):
        # return f'Data= {self.data}  L= {self._get_name(self.left)}   M= {self._get_name(self.mid)}    R= {self._get_name(self.right)}'
        return f'{self.data}'

# Used when displaying an object
    def __repr__(self):
        # return f'Data= {self.data}  L= {self._get_name(self.left)}   M= {self._get_name(self.mid)}    R= {self._get_name(self.right)}'
        return f'{self.data}'

    def _get_name(self,node):
        if node is not None:
            return node.data
        else:
            return f'No data'

    def __eq__(self, other):
        if self.data == other.data:
            return True
        else:
            return False

# Defining the nodes in the tree
# node_a1 = Node('a')
# node_a2 = Node('a')
# node_b = Node('b')
# print(f'Checking if node a1 = a2: {node_a1 == node_a2}')
# print(f'Checking if node a2 = b: {node_a2 == node_b}')

node_10 = Node(10)
node_85 = Node(85)
node_30 = Node(30)
node_7 = Node(7)
node_31 = Node(31)
node_15 = Node(15)
node_40 = Node(40)
node_63 = Node(63)
node_1 = Node(1)
node_17 = Node(17)

# Defining the node positions
node_10.left = node_85
node_10.mid = node_30
node_10.right = node_7
node_85.left = node_31
node_85.mid = node_15
node_85.right = node_40
node_30.left = node_63
node_30.mid = node_1
node_30.right = node_17

# Defining the function 'Search the Start Node and the Nodes attached to it', print the Nodes
def BFS(start_node, search_node):
    # current_node = start_node
    q = Queue.TommyQueue()
    q.push(start_node)
    print(f'Added {start_node} to start of queue')
    while q.queue:
        current_node = q.pop()
        print(f'Got {current_node} from the queue')
        if search_node == current_node:
            print(f'Found the node: {current_node}')
        else:
            if current_node.left is not None:
                q.push(current_node.left)
                print(f'Added {current_node.left} to the queue')
            if current_node.mid is not None:
                q.push(current_node.mid)
                print(f'Added {current_node.mid} to the queue')
            if current_node.right is not None:
                q.push(current_node.right)
                print(f'Added {current_node.right} to the queue')
        print(f'Current queue {q}')
    print(f'Node not found')

BFS(node_10, Node(300))
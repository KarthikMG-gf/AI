class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
root = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
root.children.append(b)
root.children.append(c)
b.children.append(d)
def display(node):
    print(node.data, end=" ")
    for child in node.children:
        display(child)
print("Decision Tree : ")
display(root)

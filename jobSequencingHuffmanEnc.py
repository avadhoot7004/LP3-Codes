class Node:
    """A Huffman Tree Node"""
    def __init__(self, freq_, symbol_, left_=None, right_=None):
        self.freq = freq_
        self.symbol = symbol_
        self.left = left_
        self.right = right_
        self.huff = ""

def print_nodes(node, val=""):
    new_val = val + str(node.huff)

    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)

    # leaf node → print code
    if not node.left and not node.right:
        print(f"{node.symbol} → {new_val}")

# characters and frequency
chars = ["a", "b", "c", "d", "e", "f"]
freq = [5, 9, 12, 13, 16, 45]

nodes = [Node(freq[x], chars[x]) for x in range(len(chars))]

while len(nodes) > 1:
    nodes = sorted(nodes, key=lambda x: x.freq)

    left = nodes[0]
    right = nodes[1]

    left.huff = "0"
    right.huff = "1"

    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

print(f"Characters : {chars}")
print(f"Frequency  : {freq}\n")
print("Huffman Encoding:")
print_nodes(nodes[0])
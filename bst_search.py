
def bst_search(node, value):
    while node is not None:
        if node.data == value:
            return node
        if node.data > value:
            node = node.left
        else:
            node = node.right

    return node

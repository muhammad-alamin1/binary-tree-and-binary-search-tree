def bst_insert(root, node):
    last_node = None
    current_node = root

    while current_node is not None:
        last_node = current_node

        if current_node.data > node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right

    if last_node is None:
        print(f'Tree was empty, node is the only node!')
        root = node
    elif last_node.data > node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)

    return root

""" Binary search tree delete node CASE Algorithm

*** If we want to delete a node from the binary search tree, it can be
1. leaf node (no child)
2. A node that has only one child
3. A node that has two child

Solution:
    first case  ---> delete node & update this node parent left or right child None
    second case ---> delete node & put the only one child in the place of this node parent
    third case  ---> To think {
                        1. search minimum and maximum node (bst_minimum)
                        2. in-order traversal (left->root->right)
                        3. if we want to delete node that has two child, then delete node & successor node transplant
                           this node position.
                        4. 
                    }

"""


def bst_minimum(root):
    while root.left is not None:
        root = root.left

    return root


node_list = []


def bst_in_order_traversal(node):
    if node.left:
        bst_in_order_traversal(node.left)

    node_list.append(node)
    print(node)

    if node.right:
        bst_in_order_traversal(node.right)


def bst_transplant(root, current_node, new_node):
    if current_node is None:
        root = new_node
    elif current_node == current_node.parent.left:
        current_node.parent.add_left(new_node)
    else:
        current_node.parent.add_right(new_node)

    return root


# bst delete
def bst_delete(root, node):
    if node.left is None:
        root = bst_transplant(root, node, node.right)
    elif node.right is None:
        root = bst_transplant(root, node, node.left)
    else:
        successor_node = bst_minimum(node.right)
        if successor_node.parent is not None:
            root = bst_transplant(root, successor_node, successor_node.right)
            successor_node.add_right(node.right)
        root = bst_transplant(root, node, successor_node)
        successor_node.add_left(node.left)

    return root


if __name__ == '__main__':
    pass
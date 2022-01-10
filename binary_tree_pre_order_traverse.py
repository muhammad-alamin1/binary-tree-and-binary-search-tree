from main import create_tree

tree_list = []


def pre_order(node):
    tree_list.append(node)

    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)


if __name__ == '__main__':
    root = create_tree()
    pre_order(root)
    print(tree_list)

# Pre-order traverse time complexity ---> O(N)
""" Pre-order traversal algorithm
    
Step 1: input tree, root
Step 2: visit root node
Step 3: traverse left sub tree --> Recursive way call  pre_order(tree, root.left)
Step 4: traverse right sub tree --> Recursive way call  pre_order(tree, root.right)

"""

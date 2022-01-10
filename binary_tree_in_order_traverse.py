from main import create_tree

tree_list = []


def in_order(node):
    if node.left:
        in_order(node.left)

    tree_list.append(node)

    if node.right:
        in_order(node.right)


if __name__ == '__main__':
    root = create_tree()
    in_order(root)
    print(tree_list)

# In order traverse complexity: O(N)
""" In-order traversal Algorithm

Step 1: input tree, root
Step 2: visit left node
Step 3: visit root node
Step 4: visit right node

"""
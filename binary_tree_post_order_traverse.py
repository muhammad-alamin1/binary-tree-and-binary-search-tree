from main import create_tree

tree_list = []


def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)

    tree_list.append(node)


if __name__ == '__main__':
    root = create_tree()
    post_order(root)
    print(tree_list)

# Post-order traverse time complexity ---> O(N)
""" Post order traversal Algorithm

Step 1: input tree, root
Step 2: traverse left sub tree --> Recursive way call post_order(tree, root.left)
Step 3: traverse right sub tree --> Recursive way call post_order(tree, root.right)
Step 4: visit root node

"""

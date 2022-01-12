from binary_search_tree import TreeNode
from bst_insert import bst_insert
from bst_search import bst_search
from bst_delete_node import bst_delete, bst_in_order_traversal
from binary_tree_in_order_traverse import in_order

"""
         _10_
        /   \
       5     17
      / \    / \
     3   7  12   19
    / \           
   1   4            
"""


def create_bst():
    root = TreeNode(10)

    node_list = [5, 17, 3, 7, 12, 19, 1, 4]
    for item in node_list:
        node = TreeNode(item)
        root = bst_insert(root, node)

    return root


if __name__ == '__main__':
    root_node = create_bst()

    for key in [7, 19]:
        result = bst_search(root_node, key)

        if result is None:
            print(f'{key} not found in Binary search tree.!')
        else:
            print(f'{key} is found in BST.')

    # delete node
    delete_item = bst_delete(root_node, result) # delete last node --> 19
    bst_in_order_traversal(root_node)

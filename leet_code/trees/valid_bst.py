"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_node(tree_list: List[int]) -> Optional[TreeNode]:
    nodes = []
    if len(tree_list) > 0:
        root = TreeNode(tree_list[0])
        nodes.append(root)
        i = 1
    else:
        return None
    while True:
        node = nodes.pop(0)
        if i < len(tree_list):
            node.left = TreeNode(tree_list[i])
            nodes.append(node.left)
            i += 1
        else:
            break
        if i < len(tree_list):
            node.right = TreeNode(tree_list[i])
            nodes.append(node.right)
            i += 1
        else:
            break
    return root


def isValidBST(root: Optional[TreeNode]) -> bool:

    return True


root = tree_node([2, 1, 3])
assert isValidBST(root), True


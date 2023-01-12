"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.
"""
from typing import Optional, List
import queue


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


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    def dive(node, d, max_d):
        if node.left:
            max_d = dive(node.left, d+1, max_d)
        if node.right:
            max_d = dive(node.right, d+1, max_d)
        if d > max_d:
            return d
        else:
            return max_d

    return dive(root, 1, 1)


def print_tree(node: TreeNode):
    print(node.val)

    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)


tl = [1, 2, 3, 4, 5, None, 6, 7, 8]
root = tree_node(tl)
max_depth(root)


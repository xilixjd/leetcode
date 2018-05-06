# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(root, mode_dict):
            if root is None:
                return None
            mode_dict[root.val] = mode_dict.get(root.val, 0) + 1
            preorder(root.left, mode_dict)
            preorder(root.right, mode_dict)

        mode_dict = {}
        res = []
        preorder(root, mode_dict)
        max_mode_count = 0
        for key in mode_dict:
            if mode_dict[key] > max_mode_count:
                max_mode_count = mode_dict[key]
        for key in mode_dict:
            if mode_dict[key] == max_mode_count:
                res.append(key)
        return res

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

solu = Solution()
print solu.findMode(root)
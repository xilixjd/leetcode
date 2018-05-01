# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def count_left_depth(root):
            depth = 0
            while root:
                root = root.left
                depth += 1
            return depth

        def count_right_depth(root):
            depth = 0
            while root:
                root = root.right
                depth += 1
            return depth

        if root is None:
            return 0
        left = count_left_depth(root)
        right = count_right_depth(root)
        if left == right:
            return 2 ** left - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
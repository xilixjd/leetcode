# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        array = [root]
        res = []
        while len(array) != 0:
            temp_array = []
            for a in array:
                if a.left:
                    temp_array.append(a.left)
                    if a.left.left is None and a.left.right is None:
                        res.append(a.left.val)
                if a.right:
                    temp_array.append(a.right)
            array = temp_array
        return sum(res)
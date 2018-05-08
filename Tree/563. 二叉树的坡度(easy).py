# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left 
subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sums_dict = {}

        def preorder(root):
            if root is None:
                return 0
            if sums_dict.get(root) is not None:
                return sums_dict.get(root)
            sums = 0
            sums += root.val
            sums += preorder(root.left)
            sums += preorder(root.right)
            sums_dict[root] = sums
            return sums

        def travel(root):
            if root is None:
                return 0
            left = preorder(root.left)
            right = preorder(root.right)
            sums = abs(left - right)
            sums += travel(root.left)
            sums += travel(root.right)
            return sums

        return travel(root)

solu = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.right.left = TreeNode(5)

print solu.findTilt(root)
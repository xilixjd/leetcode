# -*- coding:utf-8 -*-

'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import copy
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path = []
        res = []
        self.findPath(root, path, sum, res)
        return res


    def findPath(self, root, path, sum, res):
        if root is None:
            return
        path.append(root.val)
        if root.left is None and root.right is None and self.addPath(path) == sum:
            res.append(copy.copy(path))
        if root.left:
            self.findPath(root.left, path, sum, res)
        if root.right:
            self.findPath(root.right, path, sum, res)
        path.pop()


    def addPath(self, path):
        sum = 0
        for p in path:
            sum += p
        return sum

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(2)
solu = Solution()
print solu.pathSum(root, 5)
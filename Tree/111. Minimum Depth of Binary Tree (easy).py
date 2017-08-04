# -*- coding:utf-8 -*-
'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''

import copy
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        path = []
        res = []
        self.findPathMy(path, root, res)
        minDep = 100000000000
        for i in range(len(res)):
            if len(res[i]) < minDep:
                minDep = len(res[i])
        return minDep

    def findPathMy(self, path, root, res):
        if root is None:
            return
        path.append(root.val)
        if root.left is None and root.right is None:
            res.append(copy.copy(path))
        self.findPathMy(path, root.left, res)
        self.findPathMy(path, root.right, res)
        path.pop()

    def minDepth2(self, root):
        '''
        与最大深度思想类似
        :param root:
        :return:
        '''
        if root is None:
            return 0
        left = self.minDepth2(root.left)
        right = self.minDepth2(root.right)
        if not left:
            return right + 1
        if not right:
            return left + 1
        return left + 1 if left < right else right + 1


root = TreeNode(3)
# root.left = TreeNode(2)
# root.right = TreeNode(1)
solu = Solution()
print solu.minDepth2(root)
# -*- coding:utf-8 -*-

'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.


'''

import copy
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ReSolution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def back_track(root, array, res):
            if root is None:
                return
            array.append(root.val)
            if root.left is None and root.right is None:
                res.append(copy.copy(array))
            back_track(root.left, array, res)
            back_track(root.right, array, res)
            array.pop()

        res = []
        back_track(root, [], res)
        sums = 0
        for r in res:
            strs = ""
            for s in r:
                strs += str(s)
            sums += int(strs)
        return sums

root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
solu = ReSolution()
print solu.sumNumbers(None)


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        path = []
        res = []
        self.findPath(path, root, res)
        sums = 0
        for i in range(len(res)):
            sums += self.pathToInt(res[i])
        return sums

    def findPath(self, path, root, res):
        if root is None:
            return
        path.append(root.val)
        if root.left is None and root.right is None:
            res.append(copy.copy(path))
        self.findPath(path, root.left, res)
        self.findPath(path, root.right, res)
        path.pop()

    def pathToInt(self, path):
        s = ""
        for p in path:
            s += str(p)
        return int(s)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
solu = Solution()
print solu.sumNumbers(root)
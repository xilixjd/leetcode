# -*- coding:utf-8 -*-

'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

import copy


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ReSolution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def sum_array(array):
            total = 0
            for a in array:
                total += a
            return total

        def back_track(root, array, total, res):
            if root is None:
                return
            array.append(root.val)
            sums = sum_array(array)
            if sums == total and (root.left is None and root.right is None):
                res.append(copy.copy(array))
            back_track(root.left, array, total, res)
            back_track(root.right, array, total, res)
            array.pop()

        res = []
        back_track(root, [], sum, res)
        print res
        if len(res) > 0:
            return True
        else:
            return False

    def hasPathSum2(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        return self.hasPathSum2(root.left, sum) or self.hasPathSum2(root.right, sum)

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

solu = ReSolution()
print solu.hasPathSum(root, 22)


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        path = []
        res = []
        self.findPath(root, path, sum, res)
        if len(res) > 0:
            return True
        else:
            return False

    def addPath(self, path):
        sum = 0
        for p in path:
            sum += p
        return sum

    def findPath(self, root, path, sum, res):
        if root is None:
            return
        path.append(root.val)
        isLeaf = root.left is None and root.right is None
        if isLeaf and self.addPath(path) == sum:
            res.append(copy.copy(path))
        self.findPath(root.left, path, sum, res)
        self.findPath(root.right, path, sum, res)
        path.pop()

    def hasPathSum2(self, root, sum):
        if root is None:
            return False
        elif root.left is None and root.right is None and root.val == sum:
            return True
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.right = TreeNode(2)
#
# solu = Solution()
# print solu.hasPathSum(root, 8)
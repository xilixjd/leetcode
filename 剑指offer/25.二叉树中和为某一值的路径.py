# -*- coding:utf-8 -*-
'''
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''

import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None or expectNumber == 0:
            return []
        path = []
        res = []
        currentSum = 0
        self.FindPathRecur(root, expectNumber, path, res, currentSum)
        return res

    def FindPathRecur(self, root, expectNumber, path, res, currentSum):
        currentSum += root.val
        path.append(root.val)
        isLeaf = root.left is None and root.right is None
        if currentSum == expectNumber and isLeaf:
            res.append(copy.copy(path))
        if root.left is not None:
            self.FindPathRecur(root.left, expectNumber, path, res, currentSum)
        if root.right is not None:
            self.FindPathRecur(root.right, expectNumber, path, res, currentSum)
        path.pop()


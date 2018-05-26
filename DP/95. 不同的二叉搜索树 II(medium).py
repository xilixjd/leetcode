# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(start, end):
            tree_array = []
            if start > end:
                tree_array.append(None)
                return tree_array
            for i in range(start, end + 1):
                left_tree_array = generate(start, i - 1)
                right_tree_array = generate(i + 1, end)
                for j in range(len(left_tree_array)):
                    for k in range(len(right_tree_array)):
                        node = TreeNode(i)
                        node.left = left_tree_array[j]
                        node.right = right_tree_array[k]
                        tree_array.append(node)
            return tree_array

        if n <= 0:
            return []
        else:
            return generate(1, n)

# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
 

You should return [1, 3, 4].

Credits:
Special thanks to @amrsaqr for adding this problem and creating all test cases.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        array = [root]
        res = []
        while len(array) != 0:
            temp = [a.val for a in array]
            res.append(temp)
            temp = []
            for a in array:
                if a.left:
                    temp.append(a.left)
                if a.right:
                    temp.append(a.right)
            array = temp
        return [re[-1] for re in res]
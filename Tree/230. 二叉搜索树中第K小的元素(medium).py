# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? 
How would you optimize the kthSmallest routine?

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        p = root
        res = p.val
        while p:
            stack.append(p)
            p = p.left
        for i in range(k):
            x = stack.pop()
            res = x.val
            x = x.right
            while x:
                stack.append(x)
                x = x.left
        return res


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)

solu = Solution()
print solu.kthSmallest(root, 5)
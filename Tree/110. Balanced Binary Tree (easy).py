# -*- coding:utf-8 -*-
'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ReSolution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_depth(root):
            left_depth = right_depth = 1
            if root is None:
                return 0
            if root.left:
                left_depth = 1 + get_depth(root.left)
            if root.right:
                right_depth = 1 + get_depth(root.right)
            return left_depth if left_depth > right_depth else right_depth

        if root is None:
            return True
        left = get_depth(root.left)
        right = get_depth(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, node):
        if node is None:
            return 0
        left = 1
        right = 1
        left += self.height(node.left)
        right += self.height(node.right)
        return left if left > right else right
# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''

Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_depth(root):
            if root is None:
                return 0
            left_depth = right_depth = 1
            if root.left:
                left_depth += get_depth(root.left)
            if root.right:
                right_depth += get_depth(root.right)
            return left_depth if left_depth > right_depth else right_depth

        if root is None:
            return 0
        max_diameter = get_depth(root.left) + get_depth(root.right)
        max_diameter = max(max_diameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max_diameter

    def diameterOfBinaryTree2(self, root):
        self.max_diameter = 0

        def get_depth(root):
            if root is None:
                return -1
            left_depth = right_depth = 1
            left_depth += get_depth(root.left)
            right_depth += get_depth(root.right)
            if left_depth + right_depth > self.max_diameter:
                self.max_diameter = left_depth + right_depth
            return left_depth if left_depth > right_depth else right_depth

        get_depth(root)
        return self.max_diameter

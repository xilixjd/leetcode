# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure 
and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. 
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def is_same(p, q):
            if p is None:
                return q is None
            if q is None:
                return p is None
            if p.val != q.val:
                return False
            return is_same(p.left, q.left) and is_same(p.right, q.right)

        if is_same(s, t):
            return True
        else:
            if s.left and self.isSubtree(s.left, t) or s.right and self.isSubtree(s.right, t):
                return True
        return False

solu = Solution()

root = TreeNode(3)

root.left = TreeNode(1)
# root.right = TreeNode(5)
#
# root.left.left = TreeNode(1)
# root.right.left = TreeNode(2)

# root.left.right.left = TreeNode(0)

root2 = TreeNode(3)
# root2.left = TreeNode(1)
# root2.right = TreeNode(2)


print solu.isSubtree(root, root2)
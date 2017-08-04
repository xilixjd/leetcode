# -*- coding:utf-8 -*-

'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?


'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.preorder(root, res)
        return res


    def preorder(self, root, res):
        if root is None:
            return
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

solu = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
print solu.preorderTraversal(root)
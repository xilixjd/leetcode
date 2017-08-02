# -*- coding: utf-8 -*-
'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        self.inorder(root, list)
        return list


    def inorder(self, node, list):
        if node is None:
            return
        if node.left:
            self.inorder(node.left, list)
        list.append(node.val)
        if node.right:
            self.inorder(node.right, list)

r = TreeNode(1)
r.left = None

r2 = TreeNode(2)
r.right = r2
r2.left = TreeNode(3)

solu = Solution()
print solu.inorderTraversal(r)
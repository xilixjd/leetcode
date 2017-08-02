# -*- coding: utf-8 -*-

'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if not self.dfsLeft(root.left, root.val) or not self.dfsRight(root.right, root.val):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def dfsLeft(self, root, val):
        if root is None:
            return True
        if root.val >= val:
            return False
        return self.dfsLeft(root.left, val) and self.dfsLeft(root.right, val)

    def dfsRight(self, root, val):
        if root is None:
            return True
        if root.val <= val:
            return False
        return self.dfsRight(root.left, val) and self.dfsRight(root.right, val)

    def isValidBST1(self, root):
        '''
        inorder 方法
        中序遍历左节点一定比右节点小
        :param root:
        :return:
        '''
        l = []
        self.inorder(root, l)
        print l
        for i in range(1, len(l)):
            if l[i] <= l[i-1]:
                return False
        return True


    def inorder(self, root, list):
        if root is None:
           return
        self.inorder(root.left, list)
        list.append(root.val)
        self.inorder(root.right, list)

solu = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print solu.isValidBST1(root)
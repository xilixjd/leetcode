# -*- coding: utf-8 -*-
'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inorderMap = {}
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i
        return self.buildTreePostin(0, len(inorder) - 1, inorder, 0, len(postorder) - 1, postorder, inorderMap)

    # posr 和 posl 的值没搞懂
    def buildTreePostin(self, inl, inr, inorder, posl, posr, postorder, inorderMap):
        if inl > inr or posl > posr:
            return None
        root = TreeNode(postorder[posr])
        inorderIndex = inorderMap[postorder[posr]]
        root.left = self.buildTreePostin(inl, inorderIndex - 1, inorder, posl, posl + inorderIndex - inl - 1, postorder, inorderMap)
        root.right = self.buildTreePostin(inorderIndex + 1, inr, inorder, posl + inorderIndex - inl, posr - 1, postorder, inorderMap)
        return root

def inorderfunc(node):
    if node is not None:
        inorderfunc(node.left)
        # print node.val
        inorderfunc(node.right)
#
# def postorder(node):
#     if node is not None:
#         inorder(node.left)
#         inorder(node.right)
#         print node.val


inorder = [4, 2, 5, 1, 6, 3]
postorder = [4, 2, 5, 6, 3, 1]
solu = Solution()
root = solu.buildTree(inorder, postorder)
inorderfunc(root)
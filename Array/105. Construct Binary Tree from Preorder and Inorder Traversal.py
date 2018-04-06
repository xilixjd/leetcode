# -*- coding: utf-8 -*-
'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ReSolution(object):
    def buildTree(self, preorder, inorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build_tree(prel, prer, pre, inl, inr, ino, pre_ino_map):
            if prel > prer or inl > inr:
                return
            root = TreeNode(pre[prel])
            pre_index = pre_ino_map[pre[prel]]
            root.left = build_tree(prel + 1, prel + pre_index - inl, pre, inl, pre_index - 1, ino, pre_ino_map)
            root.right = build_tree(prel + pre_index - inl + 1, prer, pre, pre_index + 1, inr, ino, pre_ino_map)
            return root

        ino_map = {}
        for i in range(len(inorder)):
            ino_map[inorder[i]] = i
        root = build_tree(0, len(preorder) - 1, preorder, 0, len(inorder) - 1, inorder, ino_map)
        return root

re = ReSolution()
preorder = [1,2,4,5,3,6,8,7]
inorder = [4,2,5,1,6,8,3,7]
root = re.buildTree(preorder, inorder)
print root.right.left.right.val


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inorderMap = {}
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i
        return self.buildTreePreorder(0, len(preorder) - 1, preorder, 0, len(inorder) - 1, inorder, inorderMap)

    def buildTreePreorder(self, prel, prer, preorder, inl, inr, inorder, inorderMap):
        if prel > prer or inl > inr:
            return None
        root = TreeNode(preorder[prel])
        # 中序遍历根在前序遍历的位置
        preIndex = inorderMap[preorder[prel]]
        # preIndex - inl 左边长度
        root.left = self.buildTreePreorder(prel + 1, prel + preIndex - inl, preorder, inl, preIndex - 1, inorder, inorderMap)
        root.right = self.buildTreePreorder(prel + preIndex - inl + 1, prer, preorder, preIndex + 1, inr, inorder, inorderMap)
        return root

    def buildTreePreorderMy(self, prel, prer, preorder, inl, inr, inorder, inorderMap):
        if prel > prer or inl > inr:
            return
        root = TreeNode(preorder[prel])
        preIndex = inorderMap[preorder[prel]]
        root.left = self.buildTreePreorderMy(prel + 1, preIndex - inl + prel, preorder, inl, preIndex - 1, inorder, inorderMap)
        root.right = self.buildTreePreorderMy(preIndex - inl + prel + 1, prer, preorder, preIndex + 1, inr, inorder, inorderMap)
        return root


def inorderfunc(node):
    if node is not None:
        inorderfunc(node.left)
        print node.val
        inorderfunc(node.right)

# preorder = [1,2,4,5,3,6,8,7]
# inorder = [4,2,5,1,6,8,3,7]
# solu = Solution()
# root = solu.buildTree(preorder, inorder)
# print root.right.left.right.val
# inorderfunc(root)
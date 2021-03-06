# -*- coding:utf-8 -*-

'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        inorderMap = {}
        for i in range(len(tin)):
            inorderMap[tin[i]] = i
        return self.construct(0, len(pre) - 1, pre, 0, len(tin) - 1, tin, inorderMap)

    def construct(self, prel, prer, pre, inl, inr, tin, inorderMap):
        if prel > prer or inl > inr:
            return None
        root = TreeNode(pre[prel])
        preIndex = inorderMap[pre[prel]]
        root.left = self.construct(prel + 1, prel + preIndex - inl, pre, inl, preIndex - 1, tin, inorderMap)
        root.right = self.construct(prel + preIndex - inl + 1, prer, pre, preIndex + 1, inr, tin, inorderMap)
        return root

# -*- coding:utf-8 -*-

'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return
        deque = []
        deque.append(root)
        array = []
        while len(deque) != 0:
            pNode = deque[0]
            deque.pop(0)
            array.append(pNode.val)
            if pNode.left:
                deque.append(pNode.left)
            if pNode.right:
                deque.append(pNode.right)
        return array

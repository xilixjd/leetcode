# -*- coding:utf-8 -*-
'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        pNode = pHead
        if pNode is None:
            return None
        pDict = {}
        pCopyHead = RandomListNode(pNode.label)
        pCopy = pCopyHead
        pDict[pNode.label] = pCopy
        while pNode.next is not None:
            pCopy.next = RandomListNode(pNode.next.label)
            pCopy = pCopy.next
            pNode = pNode.next
            pDict[pNode.label] = pCopy
        pNode = pHead
        pCopy = pCopyHead
        while pNode is not None:
            if pNode.random:
                pCopy.random = pDict[pNode.random.label]
            pNode = pNode.next
            pCopy = pCopy.next
        return pCopyHead

solu = Solution()
a = RandomListNode(1)
b = RandomListNode(2)
c = RandomListNode(3)
a.next = b
b.next = c
a.random = c
print solu.Clone(a).random.label
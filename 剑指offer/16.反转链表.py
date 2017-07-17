# -*- coding:utf-8 -*-
'''
输入一个链表，反转链表后，输出链表的所有元素。

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        reverseHead = None
        first = pHead
        prev = None
        while first is not None:
            pNext = first.next
            if pNext is None:
                reverseHead = first
            first.next = prev
            prev = first
            first = pNext
        return reverseHead

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3

solu = Solution()
print solu.ReverseList(n1).next.next.val
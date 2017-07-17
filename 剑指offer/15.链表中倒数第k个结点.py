# -*- coding:utf-8 -*-

'''
输入一个链表，输出该链表中倒数第k个结点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k <= 0:
            return None
        p1 = p2 = head
        for i in range(k - 1):
            if p1.next is not None:
                p1 = p1.next
            else:
                return None
        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next
        return p2
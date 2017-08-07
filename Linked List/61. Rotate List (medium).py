# -*- coding: utf-8 -*-
'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRightMy(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n = head
        length = 0
        while n:
            length += 1
            n = n.next
        k = k % length
        if k == 0 or head is None:
            return head
        first = head
        last = head
        for i in range(k):
            first = first.next
        if not first:
            return head
        first = head
        for i in range(k - 1):
            first = first.next
        while first.next:
            first = first.next
            last = last.next
        first.next = head
        while head.next != last:
            head = head.next
        head.next = None
        return last


listNode = ListNode(1)
listNode.next = ListNode(2)
listNode.next.next = ListNode(3)
listNode.next.next.next = ListNode(4)

solu = Solution()
print solu.rotateRight(listNode, 2).next.next.next.next
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

class ReSolution(object):
    def rotateRight(self, head, k):
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
        if length == 0 or k == 0:
            return head
        k = k % length
        if k == 0 or head is None:
            return head
        root = ListNode(0)
        root.next = head
        prev = root
        p2 = p1 = head
        if p1 is None:
            return None
        for i in range(k - 1):
            p1 = p1.next
            if p1 is None:
                return None
        while p1.next:
            prev = p2
            p1 = p1.next
            p2 = p2.next
        p1.next = head
        root.next = p2
        prev.next = None
        return root.next

listNode = ListNode(1)
listNode.next = ListNode(2)
listNode.next.next = ListNode(3)
listNode.next.next.next = ListNode(4)
listNode.next.next.next.next = ListNode(5)

re = ReSolution()
print re.rotateRight(listNode, 2).val


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


# listNode = ListNode(1)
# listNode.next = ListNode(2)
# listNode.next.next = ListNode(3)
# listNode.next.next.next = ListNode(4)
#
# solu = Solution()
# print solu.rotateRightMy(listNode, 2).next.next.next.next
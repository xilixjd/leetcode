# -*- coding:utf-8 -*-
'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ReSolution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = p2 = head
        for i in range(n):
            p1 = p1.next
        if p1 is None:
            return head.next
        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next
        current = p2.next
        p2.next = current.next
        return head

root = ListNode(1)
root.next = ListNode(2)
# root.next.next = ListNode(3)
# root.next.next.next = ListNode(4)
# root.next.next.next.next = ListNode(5)
re = ReSolution()
root = re.removeNthFromEnd(root, 2)
while root is not None:
    print root.val
    root = root.next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = head
        last = head
        for i in range(n):
            first = first.next
        if not first:
            return head.next
        while first.next:
            first = first.next
            last = last.next
        last.next = last.next.next
        return head

# root = ListNode(1)
# root.next = ListNode(2)
# root.next.next = ListNode(3)
# root.next.next.next = ListNode(4)
# root.next.next.next.next = ListNode(5)

# solu = Solution()
# print solu.removeNthFromEnd(root, 1)

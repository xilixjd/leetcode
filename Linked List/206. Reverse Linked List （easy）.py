# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = root = ListNode(0)
        p1 = head
        while p1:
            p1_next = p1.next
            p1.next = pre.next
            pre.next = p1
            p1 = p1_next
        return root.next


l = ListNode(1)
# l.next = ListNode(2)
# l.next.next = ListNode(6)
# l.next.next.next = ListNode(3)
# l.next.next.next.next = ListNode(4)
# l.next.next.next.next.next = ListNode(5)
# l.next.next.next.next.next.next = ListNode(6)
re = Solution()
l = re.reverseList(None)
print l
# while l:
#     print l.val
#     l = l.next
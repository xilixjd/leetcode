# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head
        p1 = root
        while p1 and p1.next:
            temp_p1 = p1
            prev = p1
            while temp_p1.next and temp_p1.next.val == val:
                temp_p1 = temp_p1.next
            p1 = temp_p1.next
            prev.next = p1
        return root.next


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(6)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(4)
l.next.next.next.next.next = ListNode(5)
l.next.next.next.next.next.next = ListNode(6)
re = Solution()
l = re.removeElements(l, 6)
while l:
    print l.val
    l = l.next
# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = a = headA
        p2 = b = headB
        a_length = 0
        b_length = 0
        while a:
            a_length += 1
            a = a.next
        while b:
            b_length += 1
            b = b.next
        if a_length > b_length:
            for i in range(a_length - b_length):
                p1 = p1.next
        else:
            for i in range(b_length - a_length):
                p2 = p2.next
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None

    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        a = headA
        b = headB
        while a != b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a
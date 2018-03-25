# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Sort a linked list in O(n log n) time using constant space complexity.

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = head
        length = 0
        while h:
            length += 1
            h = h.next
        if length <= 1:
            return head
        p1 = head
        slow = fast = head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        p2 = slow.next
        slow.next = None
        left = self.sortList(p1)
        right = self.sortList(p2)
        return self.merge_list(left, right)

    def merge_list(self, listNode1, listNode2):
        root = ListNode(0)
        p = root
        p1 = listNode1
        p2 = listNode2
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p = p.next
                p1 = p1.next
            else:
                p.next = p2
                p = p.next
                p2 = p2.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return root.next

l = ListNode(3)
l.next = ListNode(2)
l.next.next = ListNode(4)
# l.next.next.next = ListNode(1)
re = Solution()
l = re.sortList(l)
while l:
    print l.val
    l = l.next


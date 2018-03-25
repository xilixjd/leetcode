# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        思路：
        将前一半的链表反转，再以次与后一半对比
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        pre = root = ListNode(0)
        p1 = head
        while p1 and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            p1_next = p1.next
            p1.next = pre.next
            pre.next = p1
            p1 = p1_next
        if fast:
            p2 = root.next
            p3 = slow.next
        else:
            p2 = root.next
            p3 = slow
        while p2:
            print p2.val, p3.val
            if p2.val != p3.val:
                return False
            p2 = p2.next
            p3 = p3.next
        return True

l = ListNode(1)
# l.next = ListNode(2)
# l.next.next = ListNode(3)
# l.next.next.next = ListNode(4)
# l.next.next.next.next = ListNode(4)
# l.next.next.next.next.next = ListNode(3)
# l.next.next.next.next.next.next = ListNode(2)
# l.next.next.next.next.next.next.next = ListNode(1)
re = Solution()
l = re.isPalindrome(l)
print l
# while l:
#     print l.val
#     l = l.next
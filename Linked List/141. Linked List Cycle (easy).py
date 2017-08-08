# -*- coding: utf-8 -*-

'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # if head is None:
        #     return False
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


l = ListNode(1)
# l.next = l
# l.next.next = l
# l.next.next = ListNode(3)
# l.next.next.next = l

solu = Solution()
print solu.hasCycle(l)
# -*- coding: utf-8 -*-
'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        http://blog.csdn.net/willduan1/article/details/50938210
        """
        if head is None:
            return None
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                break
        while slow != fast:
            if slow is None or fast is None:
                return None
            slow = slow.next
            fast = fast.next
        if slow.next is None:
            return None
        return slow

l = ListNode(1)
# l.next = ListNode(2)
# l.next.next = ListNode(3)
# l.next.next.next = l.next

solu = Solution()
print solu.detectCycle(l)
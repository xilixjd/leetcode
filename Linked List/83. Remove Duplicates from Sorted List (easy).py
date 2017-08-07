# -*- coding: utf-8 -*-

'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = head
        while n and n.next:
            fast = n.next
            while fast and fast.val == n.val:
                fast = fast.next
            n.next = fast
            n = n.next
        return head

listNode = ListNode(1)
# listNode.next = ListNode(1)
# listNode.next.next = ListNode(3)
# listNode.next.next.next = ListNode(4)

solu = Solution()
print solu.deleteDuplicates(listNode)
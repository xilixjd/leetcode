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


class ReSolution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        root = ListNode(0)
        prev = root
        while p:
            while p and p.next and p.val == p.next.val:
                p = p.next
            prev.next = p
            prev = p
            p = p.next
        return root.next

listNode = ListNode(1)
listNode.next = ListNode(1)
# listNode.next.next = ListNode(3)
# listNode.next.next.next = ListNode(4)

re = ReSolution()
p = re.deleteDuplicates(listNode)
while p:
    print p.val
    p = p.next




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

# listNode = ListNode(1)
# listNode.next = ListNode(1)
# listNode.next.next = ListNode(3)
# listNode.next.next.next = ListNode(4)
#
# solu = Solution()
# print solu.deleteDuplicates(listNode)
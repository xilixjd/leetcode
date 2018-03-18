# -*- coding: utf-8 -*-
'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ReSolution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head
        p = root.next
        p_prev = root
        while p is not None and p.next is not None:
            p1 = p.next
            p2 = p.next.next
            p_prev.next = p1
            p1.next = p
            p.next = p2
            p_prev = p
            p = p.next
        return root.next

listNode = ListNode(1)
listNode.next = ListNode(2)
listNode.next.next = ListNode(3)
listNode.next.next.next = ListNode(4)
# listNode.next.next.next.next = ListNode(5)

re = ReSolution()
p = re.swapPairs(listNode)
while p:
    print p.val
    p = p.next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        n = last = ListNode(0)
        n.next = head
        first = head
        second = head.next
        while first and second:
            first.next = second.next
            second.next = first
            last.next = second
            if not first.next:
                break
            if not first.next.next:
                break
            last = first
            first = first.next
            second = first.next
        print n.next.val
        return n.next

# listNode = ListNode(1)
# listNode.next = ListNode(2)
# listNode.next.next = ListNode(3)
# listNode.next.next.next = ListNode(4)
#
# solu = Solution()
# print solu.swapPairs(listNode).next.next.next.val
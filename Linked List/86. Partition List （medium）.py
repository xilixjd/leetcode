# -*- coding: utf-8 -*-
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ReSolution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = left_head = ListNode(0)
        right = right_head = ListNode(0)
        p = head
        while p:
            if p.val < x:
                left.next = p
                left = left.next
            else:
                right.next = p
                right = right.next
            p = p.next
        if right:
            right.next = None
        left.next = right_head.next
        return left_head.next

listNode = ListNode(1)
listNode.next = ListNode(4)
listNode.next.next = ListNode(3)
listNode.next.next.next = ListNode(2)
listNode.next.next.next.next = ListNode(5)
listNode.next.next.next.next.next = ListNode(2)
re = ReSolution()
# print re.partition(listNode, 3).next.next.next.next.val
p = re.partition(listNode, 3)
while p:
    print p.val
    p = p.next



class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lHead = lList = ListNode(0)
        rHead = rList = ListNode(0)
        h = head
        while h:
            if h.val < x:
                lList.next = h
                lList = h
            else:
                rList.next = h
                rList = h
            h = h.next
        rList.next = None
        lList.next = rHead.next
        return lHead.next

# listNode = ListNode(1)
# listNode.next = ListNode(4)
# listNode.next.next = ListNode(3)
# listNode.next.next.next = ListNode(2)
# listNode.next.next.next.next = ListNode(5)
# listNode.next.next.next.next.next = ListNode(2)
# solu = Solution()
# print solu.partition(listNode, 3).next.next.next.next.val
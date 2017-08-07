# -*- coding: utf-8 -*-
'''

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.


'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicatesMy(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        listNode = ListNode(0)
        listNode.next = head
        last = listNode
        n = head
        while n and n.next:
            flag = False
            end = n.next
            while end and end.val == n.val:
                end = end.next
                flag = True
            if flag:
                last.next = end
            if not flag:
                last = n
            n = end

        return listNode.next

listNode = ListNode(1)
listNode.next = ListNode(1)
listNode.next.next = ListNode(3)
listNode.next.next.next = ListNode(3)
listNode.next.next.next.next = ListNode(3)
listNode.next.next.next.next.next = ListNode(4)

solu = Solution()
print solu.deleteDuplicates(listNode).next
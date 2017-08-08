# -*- coding: utf-8 -*-
'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ? m ? n ? length of list.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        listNode = ListNode(0)
        listNode.next = head
        if m > n or head is None:
            return head
        length = 0
        h = head
        while h:
            length += 1
            h = h.next
        if m > length:
            return head
        if n > length:
            n = length
        mNode = nNode = listNode
        for i in range(m - 1):
            mNode = mNode.next
        for i in range(n - 1):
            nNode = nNode.next
        end = nNode.next.next
        reversedList, start = self.reverseList(mNode.next, nNode.next)
        mNode.next = reversedList
        start.next = end
        return listNode.next


    def reverseList(self, start, end):
        if start == end:
            return start, start
        last = start
        first = start.next
        while first != end:
            temp = first.next
            first.next = last
            last = first
            first = temp
        first.next = last
        return first, start



a = listNode = ListNode(1)
listNode.next = ListNode(4)
# a = listNode.next = ListNode(3)

solu = Solution()
print solu.reverseBetween(listNode, 1, 2).next.val
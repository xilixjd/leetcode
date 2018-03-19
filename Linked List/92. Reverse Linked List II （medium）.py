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


class ReSolution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(0)
        c_head = head
        root.next = head
        first = root
        if head is None or m > n:
            return head
        length = 0
        while c_head:
            length += 1
            c_head = c_head.next
        if length < m:
            return head
        if length < n:
            n = length
        for i in range(m - 2):
            first = first.next
        p = first.next
        prev = None
        k = n - m
        reverse_last = p
        while p and k >= 0:
            p1 = p.next
            p.next = prev
            prev = p
            p = p1
            k -= 1
        last = p
        first.next = p
        reverse_last.next = last
        return root.next


a = listNode = ListNode(1)
listNode.next = ListNode(4)
# a = listNode.next = ListNode(3)

re = ReSolution()
p = re.reverseBetween(listNode, 1, 2)
while p:
    print p.val
    p = p.next


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
# print solu.reverseBetween(listNode, 1, 2).next.val
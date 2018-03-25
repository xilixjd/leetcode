# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderListMy(self, head):
        """
        错误，Do not return anything, modify head in-place instead.
        偷鸡法
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # def reverseBetween(self, head, m, n):
        #     """
        #     :type head: ListNode
        #     :type m: int
        #     :type n: int
        #     :rtype: ListNode
        #     """
        #     root = ListNode(0)
        #     c_head = head
        #     root.next = head
        #     first = root
        #     if head is None or m > n:
        #         return head
        #     length = 0
        #     while c_head:
        #         length += 1
        #         c_head = c_head.next
        #     if length < m:
        #         return head
        #     if length < n:
        #         n = length
        #     for i in range(m - 2):
        #         first = first.next
        #     p = first.next
        #     prev = None
        #     k = n - m
        #     reverse_last = p
        #     while p and k >= 0:
        #         p1 = p.next
        #         p.next = prev
        #         prev = p
        #         p = p1
        #         k -= 1
        #     last = p
        #     first.next = p
        #     reverse_last.next = last
        #     return root.next

        array = []
        p = root = ListNode(0)
        h = head
        while h:
            array.append(h)
            h = h.next
        k = 0
        j = len(array) - 1
        while k <= j - 1:
            p.next = array[k]
            p.next.next = array[j]
            p = p.next.next
            k += 1
            j -= 1
            if k == j:
                p.next = array[k]
                p = p.next
                break
        p.next = None
        head = root.next

    def reorderList1(self, head):
        if head is None or head.next is None:
            return head
        p1 = p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        prem = p1
        prec = p1.next
        while prec.next:
            cur = prec.next
            prec.next = cur.next
            cur.next = prem.next
            prem.next = cur
        p1 = head
        p2 = prem.next
        while p1 != prem:
            prem.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = prem.next


# l = None
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
re = Solution()
re.reorderList1(l)
while l:
    print l.val
    l = l.next

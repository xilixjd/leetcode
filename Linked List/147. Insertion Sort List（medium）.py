# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Sort a linked list using insertion sort.
插入排序，即前面都是有序数组，遍历到下一个数字，将数字插入到有序数组的相应位置
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 插入排序
        # arr = [2,3,1,2,5,9,6,3,1]
        # for i in range(1, len(arr)):
        #     temp = arr[i]
        #     j = i - 1
        #     while j >= 0 and temp <= arr[j]:
        #         arr[j + 1] = arr[j]
        #         j -= 1
        #     arr[j + 1] = temp
        # print arr

        if head is None or head.next is None:
            return head
        root = ListNode(0)
        cur = head
        pre = root
        while cur:
            cur_next = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = root
            cur = cur_next
        return root.next


l = ListNode(3)
l.next = ListNode(2)
l.next.next = ListNode(4)
l.next.next.next = ListNode(1)
re = Solution()
l = re.insertionSortList(l)
while l:
    print l.val
    l = l.next

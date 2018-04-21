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


class ReSolution(object):
    def detectCycle(self, head):
        """
        思路0：
        暴力法，每遍历一个节点，检测其是否为循环初始节点
        思路1：
        每遍历一个节点，查看其是否在数组中，若是，则为初始节点，若不是，存在数组中
        time limit
        :type head: ListNode
        :rtype: ListNode
        """
        h = head
        array = []
        while h:
            if h in array:
                return h
            array.append(h)
            h = h.next
        return None

    def detectCycle2(self, head):
        """
        思路2：
        fast 和 slow 相遇的节点，slow 设为 head，接着再遍历，slow 和 fast 再相遇的节点即初始节点
        time limit
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
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
        return slow if slow and slow.next else None


l = ListNode(1)
l.next = ListNode(2)
# l.next.next = ListNode(3)
# l.next.next.next = l.next

solu = ReSolution()
print solu.detectCycle2(l)

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

# l = ListNode(1)
# l.next = ListNode(2)
# l.next.next = ListNode(3)
# l.next.next.next = l.next
#
# solu = Solution()
# print solu.detectCycle(l)
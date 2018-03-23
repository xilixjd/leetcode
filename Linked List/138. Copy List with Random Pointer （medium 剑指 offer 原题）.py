# -*- coding: utf-8 -*-
'''
A linked list is given such that each node contains an additional
random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class ReSolution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        copy_head = copy = RandomListNode(0)
        h = head
        copy_dict = {}
        while head:
            copy.next = RandomListNode(head.label)
            copy = copy.next
            copy_dict[head.label] = copy
            head = head.next
        copy = copy_head.next
        while copy:
            if h.random:
                copy.random = copy_dict[h.random.label]
            copy = copy.next
            h = h.next
        return copy_head.next

l = RandomListNode(1)
a = l.next = RandomListNode(2)
b = l.next.next = RandomListNode(3)
c = l.next.next.next = RandomListNode(4)

b.random = a
c.random = b
solu = ReSolution()
print solu.copyRandomList(l).next.next.random.label



class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        copyHead = copy = RandomListNode(1)
        copyDict = {}
        while head:
            copy.next = RandomListNode(head.label)
            copy = copy.next
            copyDict[head.label] = head
            head = head.next
        copy = copyHead.next
        while copy:
            if copyDict[copy.label].random:
                copy.random = RandomListNode(copyDict[copy.label].random.label)
            copy = copy.next
        return copyHead.next

# l = RandomListNode(1)
# a = l.next = RandomListNode(2)
# b = l.next.next = RandomListNode(3)
# c = l.next.next.next = RandomListNode(4)
#
# b.random = a
# c.random = b
# solu = Solution()
# print solu.copyRandomList(l).next.next.random.label
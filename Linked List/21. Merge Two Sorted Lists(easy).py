'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ReSolution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = root = ListNode(0)
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val < p2.val:
                n.next = p1
                p1 = p1.next
            else:
                n.next = p2
                p2 = p2.next
            n = n.next
        if p1:
            n.next = p1
        if p2:
            n.next = p2
        return root.next

n1 = ListNode(1)
n1.next = ListNode(3)
n1.next.next = ListNode(5)

n2 = ListNode(2)
n2.next = ListNode(4)
n2.next.next = ListNode(6)

re = ReSolution()
print re.mergeTwoLists(n1, n2).next.val


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next
            n = n.next
        if l1:
            n.next = l1
        if l2:
            n.next = l2
        return head.next

# n1 = ListNode(1)
# n1.next = ListNode(3)
# n1.next.next = ListNode(5)
#
# n2 = ListNode(2)
# n2.next = ListNode(4)
# n2.next.next = ListNode(6)
#
# solu = Solution()
# print solu.mergeTwoLists(n1, n2).next.val
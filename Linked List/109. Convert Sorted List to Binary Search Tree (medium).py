# -*- coding: utf-8 -*-
'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # if head is None:
        #     return None
        h = head
        nums = []
        while h:
            nums.append(h)
            h = h.next
        root = self.genBST(nums, 0, len(nums) - 1)
        return root


    def genBST(self, nums, start, end):
        if start > end:
            return
        mid = (start + end) / 2
        root = TreeNode(nums[mid].val)
        root.left = self.genBST(nums, start, mid - 1)
        root.right = self.genBST(nums, mid + 1, end)
        return root

listNode = ListNode(1)
listNode.next = ListNode(4)
listNode.next.next = ListNode(5)
listNode.next.next.next = ListNode(6)

solu = Solution()
print solu.sortedListToBST(listNode).right
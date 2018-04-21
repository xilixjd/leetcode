# -*- coding: utf-8 -*-
'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''


class ReSolution(object):
    def findDuplicate(self, nums):
        """
        https://leetcode.com/problems/find-the-duplicate-number/solution/
        先找到第一个重复的位置，再将一个数置于 nums[0]，再重新遍历，再相等即得
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

re = ReSolution()
print re.findDuplicate([1,2,1])


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for n in nums:
            if nums_dict.get(n) is None:
                nums_dict[n] = 1
            else:
                return n

    def findDplicate2(self, nums):
        # https://leetcode.com/problems/find-the-duplicate-number/solution/
        # slow = nums[0]
        # fast = nums[slow]
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        # fast = 0
        # while slow != fast:
        #     fast = nums[fast]
        #     slow = nums[slow]
        # return slow


        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        hare = nums[0]
        while tortoise != hare:
            hare = nums[hare]
            tortoise = nums[tortoise]
        return tortoise


solu = Solution()
print solu.findDplicate2([2,5,9,6,9,3,8,9,7,1])
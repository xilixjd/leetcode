# -*- coding: utf-8 -*-
'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter
what you leave beyond the new length.
'''


class ReSolution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                del nums[i - 1]
            else:
                i += 1
        return len(nums)

re = ReSolution()
print re.removeDuplicates([1,1,2,2,3,3])


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i , pre = 0, None
        while i < len(nums):
            if nums[i] != pre:
                pre = nums[i]
                i += 1
            else:
                del nums[i]
        return len(nums)

    def removeDuplicatesMy(self, nums):
        if len(nums) == 1 or len(nums) == 0:
            return len(nums)
        for i in range(1, len(nums))[::-1]:
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)

solu = Solution()
print solu.removeDuplicatesMy([1,1,2,2])
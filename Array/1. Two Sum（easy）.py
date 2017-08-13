# -*- coding: utf-8 -*-
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        暴力法
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            current = nums[i]
            diff = target - current
            for j in range(i + 1, len(nums)):
                if nums[j] == diff:
                    return [i, j]
        return None

    def twoSumFaster(self, nums, target):
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in nums_dict and nums_dict[diff] != i:
                return [i, nums_dict[diff]]
            else:
                continue
        return None

    def twoSumMy(self, nums, target):
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums_dict.get(diff) != None and nums_dict.get(diff) != i:
                return [i, nums_dict.get(diff)]
        return None


solu = Solution()
print solu.twoSum([2, 3, 8, 4, 5], 12)
print solu.twoSumMy([2, 3, 8, 4, 5], 12)
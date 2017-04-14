# -*- coding: utf-8 -*-
'''
Given an array of integers where 1 ≤ a[i] <= n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

import math

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        10% -30%
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_dict = {}
        array = []
        for n in nums:
            if nums_dict.get(n):
                nums_dict[n] += 1
            else:
                nums_dict[n] = 1

        for i in range(1, len(nums) + 1):
            if not nums_dict.get(i):
                array.append(i)
        return array

    def findDisappearedNumbersFaster(self, nums):
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]
        array = []
        for i in range(len(nums)):
            if nums[i] > 0:
                array.append(i + 1)
        return array

solu = Solution()
print solu.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print solu.findDisappearedNumbersFaster([4,3,2,7,8,2,3,1])
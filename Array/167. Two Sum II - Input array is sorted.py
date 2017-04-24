# -*- coding: utf-8 -*-
'''
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers_len = len(numbers)
        nums_dict = {}
        for i in range(numbers_len):
            nums_dict[numbers[i]] = i
        for i in range(numbers_len):
            diff = target - numbers[i]
            if diff in nums_dict and nums_dict[diff] != i:
                return [i + 1, nums_dict[diff] + 1]


solu = Solution()
print solu.twoSum([2, 3, 8, 4, 5], 12)

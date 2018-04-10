# -*- coding: utf-8 -*-

'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
'''


class ReSolution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        for i in range(len(nums)):
            if nums_dict.get(nums[i]):
                return True
            else:
                nums_dict[nums[i]] = 1
        return False


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        for n in nums:
            if nums_dict.get(n) is None:
                nums_dict[n] = 1
            else:
                return True
        return False
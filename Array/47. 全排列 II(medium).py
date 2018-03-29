# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute(nums):
            if len(nums) == 0:
                return []
            if len(nums) == 1:
                return [nums]
            res = []
            for i in range(len(nums)):
                if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                    for j in permute(nums[:i] + nums[i+1:]):
                        res.append([nums[i]] + j)
            return res

        nums.sort()
        return permute(nums)


solu = Solution()
print solu.permuteUnique([1,1,1,3])
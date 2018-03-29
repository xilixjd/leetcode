# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
import copy


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def get_subsets(start, nums, tempList, res):
            print temp_list
            res.append(copy.copy(tempList))
            for i in range(start, len(nums)):
                tempList.append(nums[i])
                get_subsets(i + 1, nums, tempList, res)
                tempList.pop()
        temp_list = []
        res = []
        get_subsets(0, nums, temp_list, res)
        return res


solu = Solution()
print solu.subsets([1,1,2])
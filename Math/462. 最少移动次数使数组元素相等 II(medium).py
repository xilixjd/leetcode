# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 
您可以假设数组的长度最多为10000。

例如:

输入:
[1,2,3]

输出:
2

说明：
只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）： 

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
'''


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        if length % 2 == 1:
            medium = nums[length // 2]
        else:
            medium = (nums[length // 2] + nums[length // 2 - 1]) / 2
        temp = [abs(n - medium) for n in nums]
        return sum(temp)
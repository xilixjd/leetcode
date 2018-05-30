# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = min_val = max_val = nums[0]
        for i in range(1, len(nums)):
            temp = max_val
            max_val = max(max(max_val * nums[i], min_val * nums[i]), nums[i])
            min_val = min(min(temp * nums[i], min_val * nums[i]), nums[i])
            res = max(res, max_val)
        return res

    def maxProduct2(self, nums):
        '''
        强行 DP
        https://leetcode.com/problems/maximum-product-subarray/discuss/133083/Java-Standard-DP-Code-with-Thinking-Process
        :param nums:
        :return:
        '''
        pass

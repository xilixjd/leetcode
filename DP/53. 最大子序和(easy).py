# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        dp[i] 为包含 nums[i] 的 0 - i 的最大子序列和
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        max_sums = dp[0]
        for i in range(1, len(dp)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_sums = max(max_sums, dp[i])
        return max_sums

solu = Solution()
print solu.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
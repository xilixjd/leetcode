# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 此方法 dp 只能用暴力法

        # dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        # for i in range(len(nums)):
        #     dp[i][i] = nums[i]
        #     # dp[0][i] = sum(nums[:i + 1])
        #
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         temp = max(dp[i][j - 1] + nums[j], dp[i][j - 1])
        #         dp[i][j] = temp
        # print dp
        # print dp[0][j]
        max_sum = nums[0]
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            if temp < nums[i]:
                temp = nums[i]
            max_sum = max(max_sum, temp)
        return max_sum


solu = Solution()
print solu.maxSubArray([-2,1,-3,4,-1,2,1,-5,6,4])
# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

class Solution(object):
    def robMy(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0 for i in range(len(nums) + 1)]
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])
        for i in range(3, len(nums) + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
        return dp[len(nums)]

solu = Solution()
print solu.rob([1, 3, 1])
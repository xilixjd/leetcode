# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [1 for i in range(len(nums))]
        max_length = 1
        for i in range(1, len(dp)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_length = max(max_length, dp[i])
        return max_length

    def lengthOfLIS2(self, nums):
        '''
        https://leetcode.com/problems/longest-increasing-subsequence/discuss/128256/beats-100-O(nlogn)-with-comments-python
        :param nums:
        :return:
        '''
        import bisect

        stack = []
        for n in nums:
            point = bisect.bisect_left(stack, n)
            if point == len(stack):
                stack.append(n)
            else:
                stack[point] = n
        return len(stack)

solu = Solution()
print solu.lengthOfLIS2([8,9,10,11,12,3,4,5,7])

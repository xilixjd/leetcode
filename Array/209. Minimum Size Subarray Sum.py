# -*- coding: utf-8 -*-

'''
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''


class Solution(object):
    def minSubArrayLenMy(self, s, nums):
        """
        最后一个测试用例通不过，时间太久
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        temp = nums
        sums = 0
        for i in range(len(nums)):
            sums = nums[i]
            j = i
            x = [nums[i]]
            while sums < s:
                j += 1
                if j > len(nums) - 1:
                    break
                sums += nums[j]
                x.append(nums[j])
            if sums >= s and len(x) <= len(temp):
                temp = x
        if sum(temp) < s:
            return 0
        else:
            return len(temp)

    def minSubArrayLenFast(self, s, nums):
        if len(nums) == 0:
            return 0
        i = j = 0
        min_num = 100000
        sums = 0
        while j < len(nums):
            sums += nums[j]
            j += 1
            while sums >= s:
                min_num = min(j - i, min_num)
                sums -= nums[i]
                i += 1
        return 0 if min_num == 100000 else min_num


solu = Solution()
print solu.minSubArrayLenFast(7, [2,3,1,2,4,3])
# -*- coding: utf-8 -*-
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                sums = 0 - nums[i]
                lo = i + 1
                hi = len(nums) - 1
                while lo < hi:
                    if sums == nums[lo] + nums[hi]:
                        res.append([nums[i], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif sums > nums[lo] + nums[hi]:
                        lo += 1
                    else:
                        hi -= 1
        return res

solu = Solution()
print solu.threeSum([1,-1,-1,0])
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


class ReSolution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                low = i + 1
                high = len(nums) - 1
                total = -nums[i]
                while low < high:
                    if nums[low] + nums[high] == total:
                        res.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < total:
                        low += 1
                    else:
                        high -= 1
        return res


solu = ReSolution()
print solu.threeSum([-1, 0, 1, 2, -1, -4])


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

    def threeSumMy(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == -nums[i]:
                        res.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < -nums[i]:
                        l += 1
                    else:
                        r -= 1
        return res

# solu = Solution()
# print solu.threeSumMy([0, 0])
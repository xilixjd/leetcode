# -*- coding: utf-8 -*-

'''
Given an array S of n integers, are there elements a, b, c,
and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution(object):
    def fourSumMy(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                sums = target - nums[i] - nums[j]
                lo = j + 1
                hi = len(nums) - 1
                print nums[i], nums[j], nums[lo], nums[hi]
                while lo < hi:
                    if nums[lo] + nums[hi] == sums:
                        if not [nums[i], nums[j], nums[lo], nums[hi]] in res:
                            res.append([nums[i], nums[j], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] > sums:
                        hi -= 1
                    else:
                        lo += 1
        return res

    def fourSumMy2(self, nums, target):
        nums.sort()
        print nums
        res = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                l = j + 1
                r = len(nums) - 1
                print i, j, l, r
                while l < r:
                    sums = nums[i] + nums[j] + nums[l] + nums[r]
                    if sums == target:
                        if [nums[i], nums[j], nums[l], nums[r]] not in res:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif sums < target:
                        l += 1
                    else:
                        r -= 1
        return res

solu = Solution()
print solu.fourSumMy2([-1,0,1,2,-1,-4], -1)
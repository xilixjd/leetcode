# -*- coding: utf-8 -*-

'''
Given an array S of n integers, find three integers in S such that the sum is closest to a
given number, target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class ReSolution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_diff = 100000000
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                low = i + 1
                high = len(nums) - 1
                while low < high:
                    diff = target - nums[i] - nums[low] - nums[high]
                    if abs(diff) < abs(min_diff):
                        min_diff = diff
                    if diff == 0:
                        return target
                    elif diff > 0:
                        low += 1
                    else:
                        high -= 1
        print target, min_diff
        return target - min_diff


solu = ReSolution()
print solu.threeSumClosest([0, 2, 1, -3], 1)


class Solution(object):
    def threeSumClosestMy(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        # min_diff = nums[0] + nums[-2] + nums[-1]
        min_diff = 1000000000
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                lo = i + 1
                hi = len(nums) - 1
                while lo < hi:
                    diff = nums[i] + nums[lo] + nums[hi] - target
                    print nums[i], nums[lo], nums[hi], diff
                    if diff == 0:
                        return target
                    # elif abs(diff) > abs(min_diff):
                    #     min_diff = diff
                    #     while lo < hi and nums[lo] == nums[lo + 1]:
                    #         lo += 1
                    #     while lo < hi and nums[hi] == nums[hi - 1]:
                    #         hi -= 1
                    #     hi -= 1
                    elif abs(diff) < abs(min_diff):
                        min_diff = diff
                        # 加了之后 最后两个测试样例通不过（某一个是以下的测试样例）
                        # while lo < hi and nums[lo] == nums[lo + 1]:
                        #     lo += 1
                        # while lo < hi and nums[hi] == nums[hi - 1]:
                        #     hi -= 1
                    if diff < 0:
                        lo += 1
                    else:
                        hi -= 1
        print min_diff
        return min_diff + target

    def threeSumClosestMy2(self, nums, target):
        nums.sort()
        min_diff = 100000000
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    sums = nums[i] + nums[l] + nums[r]
                    diff = sums - target
                    if diff == 0:
                        return target
                    elif abs(diff) < abs(min_diff):
                        min_diff = diff
                    if diff < 0:
                        l += 1
                    else:
                        r -= 1
        return min_diff + target

# solu = Solution()
# print solu.threeSumClosestMy2([13,2,0,-14,-20], -20)
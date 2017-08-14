# -*- coding: utf-8 -*-

'''
Given an array S of n integers, find three integers in S such that the sum is closest to a
given number, target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


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

solu = Solution()
print solu.threeSumClosestMy2([13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6], -59)
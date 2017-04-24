# -*- coding: utf-8 -*-
'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''


class Solution(object):
    def findPeakElementMy(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array = []
        nums.append(-214748364845)
        for i in range(1, len(nums)):
            j = i
            while nums[j] > nums[j - 1]:
                j += 1
            array.append(j - 1)
        if len(nums) == 1:
            return nums[0]
        return array[0]

    def findPeakElementMyFast(self, nums):
        nums.append(-214748364845)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                continue
            else:
                return i - 1



    # 3.二分法

solu = Solution()
print solu.findPeakElementMyFast([1,2,3,1])
# -*- coding: utf-8 -*-
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

Subscribe to see which companies asked this question.
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] < 0:
                return nums[i]
        return nums[0]

    # 2.二分法
    def findMinFast(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            mid = (start + end) / 2
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid
        return nums[start]

    def findMinMy(self, nums):
        p1 = 0
        p2 = len(nums) - 1
        while p1 < p2:
            if nums[p1] < nums[p2]:
                return nums[p1]
            mid = (p1 + p2) / 2
            if nums[mid] >= nums[p1]:
                p1 = mid + 1
            else:
                p2 = mid
        return nums[p1]


solu = Solution()
print solu.findMinMy([1,2])
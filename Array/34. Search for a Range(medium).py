# -*- coding: utf-8 -*-
'''
Given an array of integers sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solution(object):
    def searchRange1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        https://yq.aliyun.com/articles/860
        1. 不用二分法
        """
        l = 0
        r = len(nums) - 1
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        while l < r:
            if nums[l] < target:
                l += 1
            if nums[r] > target:
                r -= 1
            if nums[l] == target and nums[r] == target:
                return [l, r]
        return [-1, -1]

    def searchRange2(self, nums, target):
        '''
        2. 用二分法
        可参考 《剑指 offer》 的 p205
        :param nums:
        :param target:
        :return:
        '''
        first = self.binarySearchFirst(nums, target)
        last = self.binarySearchLast(nums, target)
        return [first, last]

    def binarySearchFirst(self, nums, target):
        start = 0
        end = len(nums) - 1
        idx = -1
        while start <= end:
            mid = (start + end) / 2
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
            if nums[mid] == target:
                idx = mid
        return idx

    def binarySearchLast(self, nums, target):
        start = 0
        end = len(nums) - 1
        idx = -1
        while start <= end:
            mid = (start + end) / 2
            if target >= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
            if nums[mid] == target:
                idx = mid
        return idx

    def binarySearch(self, i, j, nums, target):
        mid = (i + j) / 2
        if mid < 0:
            return -1
        if mid != 0 and mid + 1 > j:
            return -1
        if nums[mid] > target:
            return self.binarySearch(i, mid - 1, nums, target)
        elif nums[mid] < target:
            return self.binarySearch(mid + 1, j, nums, target)
        else:
            return mid

solu = Solution()
print solu.searchRange1([1], 1)
print solu.binarySearch(0, 0, [1], 1)
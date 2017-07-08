# -*- coding: utf-8 -*-
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.
'''

class Solution(object):
    def search(self, nums, target):
        """
        没理解题意就是 find 的话也太简单了
        应该是还要求 logn 的时间复杂度
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        array = []
        i = 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                array += nums[i:]
                break
            i += 1
        if i == len(nums):
            array = nums
        else:
            array += nums[:i]
        start = 0
        end = len(array) - 1
        print array
        while start + 1 < end:
            mid = int((start + end) / 2)
            if array[mid] == target:
                start = mid
            elif array[mid] < target:
                start = mid
            else:
                end = mid
        if array[start] == target:
            return start
        if array[end] == target:
            return end
        return -1

    def binarySearch(self, i, j, nums, target):
        mid = (i + j) / 2
        if nums[mid] < target:
            return self.binarySearch(i, mid - 1, nums, target)
        elif nums[mid] > target:
            return self.binarySearch(mid + 1, j, nums, target)
        else:
            return mid

solu = Solution()
print solu.search([4,5,6,7,0,1,2], 2)
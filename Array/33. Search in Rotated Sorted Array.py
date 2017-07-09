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
        此题在 《剑指 offer》p69 有启发
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        if target < nums[i]:
            for index in range(j + 1)[::-1]:
                if nums[index] == target:
                    return index
        elif target > nums[i]:
            for index in range(j + 1):
                if nums[index] == target:
                    return index
        else:
            return i
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

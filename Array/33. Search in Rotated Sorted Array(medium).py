# -*- coding: utf-8 -*-
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.
'''


class ReSolution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(nums, low, high, target):
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    return mid
            return -1

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        low = 0
        high = len(nums) - 1
        while nums[low] >= nums[high]:
            if high - low == 1:
                break
            mid = (low + high) / 2
            if nums[low] <= nums[mid]:
                low = mid
            if nums[high] >= nums[mid]:
                high = mid
        if nums[0] <= target <= nums[high - 1]:
            index = binary_search(nums, 0, high - 1, target)
        else:
            index = binary_search(nums, high, len(nums) - 1, target)
        return index

    def search2(self, nums, target):
        '''
        更好的解法
        :param nums:
        :param target:
        :return:
        '''
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


re = ReSolution()
print re.search([1], 1)


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
        if len(nums) == 0:
            return -1
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

    def searchMy(self, nums, target):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        i = 0
        j = len(nums) - 1
        while nums[i] >= nums[j]:
            if j - i == 1:
                break
            mid = (i + j) / 2
            if nums[mid] >= nums[i]:
                i = mid
            if nums[mid] <= nums[j]:
                j = mid
        if nums[j] <= target <= nums[len(nums)-1]:
            index = self.binarySearch(nums[j:], target)
            if index != -1:
                index += j
            return index
        else:
            index = self.binarySearch(nums[:j], target)
            return index


    def binarySearch(self, nums, target):
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) / 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                return mid
        return -1


solu = Solution()
print solu.searchMy([1], 1)
# print solu.binarySearch([1,2,3,4,5,6,7], 7)

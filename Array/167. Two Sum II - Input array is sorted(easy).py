# -*- coding: utf-8 -*-
'''
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''


class ReSolution(object):
    def twoSum(self, numbers, target):
        """
        二分法 6%
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(nums, low, high, target):
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        for i in range(len(numbers) - 1):
            ano_target = target - numbers[i]
            ano_index = binary_search(numbers, i + 1, len(numbers) - 1, ano_target)
            if ano_index != -1:
                return [i + 1, ano_index + 1]
        return [-1, -1]

    def twoSum2(self, numbers, target):
        '''
        https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51239/Share-my-java-AC-solution.
        :param numbers:
        :param target:
        :return:
        '''
        low = 0
        high = len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            elif total > target:
                high -= 1
            else:
                low += 1



re = ReSolution()
print re.twoSum([2, 3, 8, 4, 5], 12)


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers_len = len(numbers)
        nums_dict = {}
        for i in range(numbers_len):
            nums_dict[numbers[i]] = i
        for i in range(numbers_len):
            diff = target - numbers[i]
            if diff in nums_dict and nums_dict[diff] != i:
                return [i + 1, nums_dict[diff] + 1]


solu = Solution()
# print solu.twoSum([2, 3, 8, 4, 5], 12)

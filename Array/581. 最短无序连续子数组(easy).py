# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''

import copy


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        8.5%
        此思路与答案中 O(n) 的思路很像，只是没有用栈，用栈能减少很多不必要的遍历
        :type nums: List[int]
        :rtype: int
        """
        left_min = 0
        left_left = len(nums) - 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1] and nums[i] < nums[left_min]:
                left_left = 0
                break
            elif nums[i] < nums[i - 1]:
                left = i
                while nums[i] < nums[left - 1]:
                    left -= 1
                if left < left_left:
                    left_left = left
            if nums[i] < nums[left_min]:
                left_min = i
        if left_left == len(nums) - 1:
            return 0
        right_max = len(nums) - 1
        right_right = 0
        for i in range(len(nums) - 1)[::-1]:
            if nums[i] > nums[i + 1] and nums[i] > nums[right_max]:
                right_right = len(nums) - 1
                break
            elif nums[i] > nums[i + 1]:
                right = i
                while nums[right + 1] < nums[i]:
                    right += 1
                if right > right_right:
                    right_right = right
            if nums[i] > nums[right_max]:
                right_max = i
        if right_right == 0:
            return 0
        return right_right - left_left + 1

    def findUnsortedSubarray2(self, nums):
        '''
        排序，对比
        :param nums:
        :return:
        '''
        temp_nums = copy.copy(nums)
        temp_nums.sort()
        left = len(nums) - 1
        if left == 0:
            return 0
        right = 0
        for i in range(len(nums)):
            if nums[i] != temp_nums[i]:
                left = i
                break
        for j in range(len(nums))[::-1]:
            if nums[j] != temp_nums[j]:
                right = j
                break
        print left, right
        return 0 if right < left else right - left + 1

    def findUnsortedSubarray3(self, nums):
        '''
        用 stack
        :param nums:
        :return:
        '''
        stack = []
        left = len(nums) - 1
        right = 0
        for i in range(len(nums)):
            while len(stack) != 0 and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)
        stack = []
        for j in range(len(nums))[::-1]:
            while len(stack) != 0 and nums[stack[-1]] < nums[j]:
                right = max(right, stack.pop())
            stack.append(j)
        return 0 if left > right else right - left + 1

solu = Solution()
print solu.findUnsortedSubarray3([3,1])
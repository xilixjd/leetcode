# -*- coding: utf-8 -*-
'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
 The algorithm should run in linear time and in O(1) space.
'''

import math
class Solution(object):
    def majorityElementMy(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        nums_dict = {}
        array = []
        appear_time = math.floor(nums_len / 3) + 1
        for i in range(nums_len):
            if nums_dict.get(nums[i]) is None:
                nums_dict[nums[i]] = 1
            else:
                nums_dict[nums[i]] += 1
        for k in nums_dict:
            if nums_dict[k] >= appear_time:
                array.append(k)
        return array

    def majorityElementFast(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]

solu = Solution()
print solu.majorityElement([1,1,3,1])
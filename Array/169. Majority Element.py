# -*- coding: utf-8 -*-
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = nums[0]
        count = 1
        k = 0
        for n in nums[1:]:
            if count == 0:
                majority = n
                count += 1
            elif majority == n:
                count += 1
            else:
                count -= 1
        return majority

    def majorityElementMy(self, nums):
        length = len(nums)
        if length == 0:
            return
        nums_dict = {}
        for i in range(len(nums)):
            if nums_dict.get(nums[i]) is None:
                nums_dict[nums[i]] = 1
                if nums_dict[nums[i]] > length / 2:
                    return nums[i]
            else:
                nums_dict[nums[i]] += 1
                if nums_dict[nums[i]] > length / 2:
                    return nums[i]

solu = Solution()
print solu.majorityElement([1,3,5,2,3,4,6])
# -*- coding: utf-8 -*-
'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
'''

class Solution(object):
    def missingNumberMy(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        nums_dict = {}
        for i in range(nums_len):
            nums_dict[nums[i]] = 1
        for j in range(nums_len + 1):
            if nums_dict.get(j) is None:
                return j

    def missingNumber(self, nums):
        #  a^b^b =a
        xor = 0
        i = 0
        for n in nums:
            xor = xor ^ i ^ n
            i += 1
        return i ^ xor

    def missingNumber2(self, nums):
        #  等差数列求和 再减去所有 nums 数组的值
        nums_len = len(nums)
        sum = (0 + nums_len) * (nums_len + 1) / 2
        for n in nums:
            sum -= n
        return sum


solu = Solution()
print solu.missingNumber2([0, 1])
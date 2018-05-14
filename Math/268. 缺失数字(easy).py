# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        the_num = 0
        for i in range(len(nums) + 1):
            the_num ^= i
        for i in range(len(nums)):
            the_num ^= nums[i]
        return the_num

solu = Solution()
print solu.missingNumber([3,0,1])
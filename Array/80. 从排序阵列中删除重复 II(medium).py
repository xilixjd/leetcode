# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        temp = False
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                if temp:
                    del nums[i - 1]
                else:
                    temp = True
                    i += 1
            else:
                i += 1
                temp = False
        print nums
        return len(nums)

solu = Solution()
print solu.removeDuplicates([1,1,2,2,2,3])
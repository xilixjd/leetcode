# -*- coding: utf-8 -*-
'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_dict = {}
        array = []
        for n in nums:
            if nums_dict.get(n):
                nums_dict[n] += 1
            else:
                nums_dict[n] = 1

        for k in nums_dict:
            if nums_dict[k] > 1:
                array.append(k)
        return array

solu = Solution()
print solu.findDuplicates([4,3,2,7,8,2,3,1])
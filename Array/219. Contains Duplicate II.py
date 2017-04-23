# -*- coding: utf-8 -*-
'''
Given an array of integers and an integer k,
 find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
 and the absolute difference between i and j is at most k.

'''


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_dict = {}
        for i, v in enumerate(nums):
            if v in nums_dict and i - nums_dict[v] <= k:
                return True
            else:
                nums_dict[v] = i
        return False


solu = Solution()
print solu.containsNearbyDuplicate([1,0,1,1], 1)
# -*- coding: utf-8 -*-

'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for n in nums:
            if nums_dict.get(n) is None:
                nums_dict[n] = set([n])
        for key in nums_dict:
            print key
            if key + 1 in nums_dict:
                nums_dict[key + 1] |= nums_dict[key]
                nums_dict[key] |= nums_dict[key + 1]
            if key - 1 in nums_dict:
                nums_dict[key - 1] |= nums_dict[key]
                nums_dict[key] |= nums_dict[key - 1]
        max_len = 0
        for key in nums_dict:
            max_len = max(max_len, len(nums_dict[key]))

        # print nums_dict
        print max_len
        return max_len


solu = Solution()
solu.longestConsecutive([-9,-4,9,-7,0,7,3,-1,6,2,-2,8,-2,0,2,-7,-5,-2,6,-5,0,-8,8,1,0,6,8,-8,-1])
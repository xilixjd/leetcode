# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
'''
import copy


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(s):
            return s == s[::-1]

        def back_track(start, nums, tempList, res):
            if start == len(nums):
                res.append(copy.copy(tempList))
            for i in range(start, len(nums)):
                if is_palindrome(nums[start: i + 1]):
                    tempList.append(nums[start: i + 1])
                    back_track(i + 1, nums, tempList, res)
                    tempList.pop()

        res = []
        back_track(0, s, [], res)
        return res

re = Solution()
print re.partition("aabb")
# -*- coding: utf-8 -*-

'''
Given a collection of integers that might contain duplicates,
nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

import copy


class ReSolution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def get_subsets(start, nums, tempList, res):
            res.append(copy.copy(tempList))
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i - 1]:
                    continue
                tempList.append(nums[i])
                print temp_list, i, start
                get_subsets(i + 1, nums, tempList, res)
                tempList.pop()

        temp_list = []
        res = []
        nums.sort()
        get_subsets(0, nums, temp_list, res)
        return res

re = ReSolution()
print re.subsetsWithDup(['a', 'a', 'b'])


class Solution(object):
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res

    def subsetsWithDupMy(self, S):
        result = []
        l = []
        S.sort()
        self.backTrack(result, l, S, 0)
        return result

    def backTrack(self, result, l, S, start):
        result.append(copy.copy(l))
        for i in range(start, len(S)):
            if i != start and S[i] == S[i-1]:
                continue
            l.append(S[i])
            print 'before', l
            self.backTrack(result, l, S, i+1)
            print 'after', l
            l.pop()

solu = Solution()
# print solu.subsetsWithDupMy([1, 2, 2, 1])
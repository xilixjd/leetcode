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
print solu.subsetsWithDupMy([1, 2, 2, 1])
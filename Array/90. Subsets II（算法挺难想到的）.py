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


class Solution(object):
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                print j, res[j], [S[i]], res[j] + [S[i]]
                res.append(res[j] + [S[i]])
        return res

solu = Solution()
print solu.subsetsWithDup([1, 2, 2, 1])
# -*- coding: utf-8 -*-
'''
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''

import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        temList = []
        self.backTrack(res, candidates, temList, target, 0)
        print res
        return res

    def backTrack(self, res, numList, temList, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            res.append(copy.copy(temList))
        else:
            for i in range(start, len(numList)):
                if start != i and numList[i] == numList[i-1]:
                    continue
                temList.append(numList[i])
                self.backTrack(res, numList, temList, remain - numList[i], i + 1)
                temList.pop()


solu = Solution()
print solu.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
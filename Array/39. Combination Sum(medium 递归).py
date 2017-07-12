# -*- coding: utf-8 -*-

'''
Given a set of candidate numbers (C) (without duplicates) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        temList = []
        return self.backTrack(res, candidates, temList, target, 0)
        # return res

    def backTrack(self, res, numList, temList, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            res.append(temList)
            print temList
        else:
            for i in range(start, len(numList)):
                temList.append(numList[i])
                self.backTrack(res, numList, temList, remain - numList[i], i)
                temList.pop()
        return res

solu = Solution()
print solu.combinationSum([2, 3, 6, 7], 7)
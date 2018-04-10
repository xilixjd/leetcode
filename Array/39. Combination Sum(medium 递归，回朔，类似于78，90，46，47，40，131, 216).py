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

import copy


class ReSolution(object):
    def combinationSum(self, candidates, target):
        """
        回朔法，与以下几题有关联
        https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def back_track(start, candidates, remain, tempList, res):
            if remain < 0:
                return
            if remain == 0:
                res.append(copy.copy(tempList))
            for i in range(start, len(candidates)):
                tempList.append(candidates[i])
                back_track(i, candidates, remain - candidates[i], tempList, res)
                tempList.pop()

        tempList = []
        res = []
        candidates.sort()
        back_track(0, candidates, target, tempList, res)
        return res


re = ReSolution()
print re.combinationSum([10, 1, 2, 7, 6, 1, 5], 8)



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
        self.backTrack(res, candidates, temList, target, 0)
        return res

    def backTrack(self, res, numList, temList, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            res.append(copy.copy(temList))
        else:
            for i in range(start, len(numList)):
                temList.append(numList[i])
                self.backTrack(res, numList, temList, remain - numList[i], i)
                temList.pop()

    def combinationSumMy(self, candidates, target):
        candidates.sort()
        res = []
        temList = []
        self.backTrackMy(res, candidates, temList, target, 0)
        return res

    def backTrackMy(self, res, numList, temList, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            res.append(copy.copy(temList))
        else:
            for i in range(start, len(numList)):
                temList.append(numList[i])
                self.backTrackMy(res, numList, temList, remain - numList[i], i)
                temList.pop()


solu = Solution()
print solu.combinationSum([2, 3, 6, 7], 7)
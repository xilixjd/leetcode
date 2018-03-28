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


class ReSolution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def back_track(start, candidates, remain, tempList, res):
            if remain == 0:
                # if tempList not in res:
                res.append(copy.copy(tempList))
            if remain < 0:
                return
            for i in range(start, len(candidates)):
                if i != start and candidates[i] == candidates[i - 1]:
                    continue
                tempList.append(candidates[i])
                back_track(i + 1, candidates, remain - candidates[i], tempList, res)
                tempList.pop()

        res = []
        tempList = []
        candidates.sort()
        back_track(0, candidates, target, tempList, res)
        return res

re = ReSolution()
print re.combinationSum([2,2,2], 4)


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
        self.backTrackMy(res, candidates, temList, target, 0)
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

    def backTrackMy(self, res, numList, temList, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            res.append(copy.copy(temList))
        else:
            for i in range(start, len(numList)):
                # 如 [1, 2, 5] 1 可以为 第一个或第二个，加这一行可避免这种情况
                if i != start and numList[i] == numList[i-1]:
                    continue
                temList.append(numList[i])
                print i, temList
                self.backTrackMy(res, numList, temList, remain - numList[i], i + 1)
                temList.pop()


solu = Solution()
print solu.combinationSum2([2,2,2], 4)
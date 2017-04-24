# -*- coding: utf-8 -*-
'''
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

'''


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.findCombo(xrange(1, 10), k, n, 0, res, [])
        return res

    def findCombo(self, nums, k, n, pos, res, tmp):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            res.append(tmp)
        for i in xrange(pos, len(nums)):
            self.findCombo(nums, k-1, n-nums[i], i+1, res, tmp+[nums[i]])


class Solution2(object):
    def combinationSum3(self, k, n):
        res = []
        self.dfs(xrange(1, 10), k, n, 0, [], res)
        return res

    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0:  # backtracking
            return
        if k == 0 and n == 0:
            res.append(path)
            print res
        for i in xrange(index, len(nums)):
            self.dfs(nums, k - 1, n - nums[i], i + 1, path + [nums[i]], res)

solu = Solution()
print solu.combinationSum3(3, 9)
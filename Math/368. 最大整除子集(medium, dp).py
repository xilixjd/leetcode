# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

给出一个由无重复的正整数组成的集合, 找出其中最大的整除子集, 子集中任意一对 (Si, Sj) 都要满足: 
Si % Sj = 0 或 Sj % Si = 0。

如果有多个目标子集，返回其中任何一个均可。

示例 1:

集合: [1,2,3]

结果: [1,2] (当然, [1,3] 也正确)
 示例 2:

集合: [1,2,4,8]

结果: [1,2,4,8]
'''


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dp = [1 for i in range(len(nums))]
        last = [-1 for i in range(len(nums))]
        nums.sort()
        idx = max_num = 0
        for i in range(len(dp)):
            for j in range(i):
                print nums[i], nums[j]
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    last[i] = j
            if max_num < dp[i]:
                max_num = dp[i]
                idx = i
        res = []
        while idx != -1:
            res.append(nums[idx])
            idx = last[idx]
        return res

solu = Solution()
print solu.largestDivisibleSubset([4,8,10,240])
# print solu.largestDivisibleSubset([1,2,3,4])

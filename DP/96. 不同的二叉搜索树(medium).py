# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


class Solution(object):
    def numTrees(self, n):
        """
        n == 3 时，
        要算出以 1 为根节点的二叉搜索树的数量 g(0) * g(2)
        以 2 为根节点的二叉搜索树的数量 g(1) * g(1)
        以 3 为根节点的二叉搜索树的数量 g(2) * g(0)
        相加
        :type n: int
        :rtype: int
        """
        # 递归超时
        # if n == 0 or n == 1:
        #     return 1
        # result = 0
        # for i in range(1, n + 1):
        #     result += self.numTrees(i - 1) * self.numTrees(n - i)
        # return result
        if n == 0 or n == 1:
            return 1
        dp = [0 for i in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(2, len(dp)):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]

solu = Solution()
print solu.numTrees(0)
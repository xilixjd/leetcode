# -*- coding: utf-8 -*-
'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        http://blog.csdn.net/u012501459/article/details/46622501
        递归超时
        """
        if n == 0 or n == 1:
            return 1
        result = 0
        for i in range(n):
            result += self.numTrees(i) * self.numTrees(n - i - 1)
        return result

    def numTrees2(self, n):
        '''
        http://blog.csdn.net/u012501459/article/details/46622501
        :param n:
        :return:
        '''
        g = [0 for i in range(n + 1)]
        g[0] = 1
        g[1] = 1
        for i in range(2, n+1):
            for j in range(0, i):
                g[i] += g[j] * g[i-j-1]
        return g[n]


solu = Solution()
print solu.numTrees2(3)
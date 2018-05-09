# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
'''
import copy


class Solution(object):
    def getPermutation(self, n, k):
        """
        https://blog.csdn.net/ChilseaSai/article/details/49129663
        https://www.cnblogs.com/jdneo/p/5305212.html
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = 1
        for i in range(2, n):
            factorial *= i
        n_list = [i + 1 for i in range(n)]
        rount = n - 1
        res = ""
        k -= 1
        while rount >= 0:
            num = n_list[k / factorial]
            res += str(num)
            n_list.pop(k / factorial)
            if rount > 0:
                k = k % factorial
                factorial /= rount
            rount -= 1
        return res


solu = Solution()
print solu.getPermutation(1, 1)
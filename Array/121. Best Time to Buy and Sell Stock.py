# -*- coding: utf-8 -*-

'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''


class Solution(object):
    def maxProfitMy(self, prices):
        """
        出错，超时！
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(len(prices)):
            max_num = -10000000
            min_num = 10000000
            if prices[i] < min_num:
                min_num = prices[i]
            if i == len(prices) - 1:
                break
            for j in range(i + 1, len(prices)):
                if prices[j] > max_num:
                    max_num = prices[j]
            max_profit = max(max_num - min_num, max_profit)
        return max_profit

    def maxProfitMy2(self, prices):
        max_profit = 0
        max_num_dict = {}
        min_num_dict = {}
        for i in range(len(prices)):


solu = Solution()
print solu.maxProfitMy([7,6,4,3,1])
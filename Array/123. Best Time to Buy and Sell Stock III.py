# -*- coding: utf-8 -*-
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        DP 方法：
        buy1 是你第一支买股票要花的钱，所以越少越好，由于是负的，所以用 max
        sell1 是你第一支卖股票的钱，你将得到 prices[i] + buy1 由于 buy1 为负 所以用 +
        buy2 是你第二支买股票要花的钱，越少越好
        sell2 是你第二支卖股票要得到的钱，越多越好
        :type prices: List[int]
        :rtype: int
        """
        sell1 = sell2 = 0
        buy1 = buy2 = -100000000
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
        return sell2

solu = Solution()
print solu.maxProfit([7,5,4,10,3,2,1,10])
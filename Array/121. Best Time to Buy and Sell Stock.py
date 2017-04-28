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
        '''
        效率较低 9%
        :param prices:
        :return:
        '''
        max_profit = 0
        if len(prices) == 0 or len(prices) == 1:
            return 0
        max_num_dict = {0: prices[0]}
        min_num_dict = {1: prices[1]}
        for i in range(len(prices)):
            max_pos = max_num_dict.keys()[0]
            min_pos = min_num_dict.keys()[0]
            if prices[i] < min_num_dict[min_pos]:
                min_num_dict = {i: prices[i]}
                min_pos = min_num_dict.keys()[0]
            if prices[i] >= max_num_dict[max_pos] or max_pos <= min_pos:
                max_num_dict = {i: prices[i]}
                max_pos = max_num_dict.keys()[0]
            print max_num_dict
            print min_num_dict
            if max_pos > min_pos:
                max_profit = max(max_profit, max_num_dict[max_pos] - min_num_dict[min_pos])
        return max_profit

    def maxProfitMyFast(self, prices):
        '''
        Kadane's Algorithm
        :param prices:
        :return:
        '''
        maxCur = maxSoFar = 0
        for i in range(1, len(prices)):
            maxCur = max(0, maxCur + prices[i] - prices[i - 1])
            maxSoFar = max(maxSoFar, maxCur)
        return maxSoFar

    def maxProfitMyFaster(self, prices):
        minPrice = 10000000
        maxPro = 0
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxPro = max(maxPro, prices[i] - minPrice)
        return maxPro

solu = Solution()
print solu.maxProfitMyFaster([7,5,4,10,3,2,1,10])
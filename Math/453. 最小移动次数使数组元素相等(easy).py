# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。

示例:

输入:
[1,2,3]

输出:
3

解释:
只需要3次移动（注意每次移动会增加两个元素的值）：

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
'''


class Solution(object):
    def minMoves(self, nums):
        """
        https://leetcode.com/problems/minimum-moves-to-equal-array-elements/discuss/93817/It-is-a-math-question
        m 为移动次数，sums 为 sum(nums)，x 为移动后的数组中的数，n 为数组长度，min_num 为 min(nums)，则有
        x * n = sums + (n - 1) * m
        x = min_num + m
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)

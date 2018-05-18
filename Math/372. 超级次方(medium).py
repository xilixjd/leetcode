# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

示例 1:

a = 2
b = [3]

结果: 8
示例 2:

a = 2
b = [1,0]

结果: 1024

'''


class Solution(object):
    def superPow(self, a, b):
        '''
        https://leetcode.com/problems/super-pow/discuss/84467/Simple-python-solution-using-recursion
        (a * b) % 1337 = ((a % 1337) * (b % 1337)) % 1337

        :param a:
        :param b:
        :return:
        '''
        # if not b:
        #     return 1
        # return pow(a, b.pop(), 1337)*self.superPow(pow(a, 10, 1337), b)%1337
        if len(b) == 0:
            return 1
        return pow(a, b.pop(), 1337) * self.superPow(pow(a, 10, 1337), b) % 1337

solu = Solution()
print solu.superPow(10, [1,2])
# -*- coding:utf-8 -*-
'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
class Solution:
    def NumberOf1(self, n):
        '''
        不能判断负数
        :param n:
        :return:
        '''
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count

    def NumberOf12(self, n):
        count = 0
        while n:
            count += 1
            n = (n - 1) & n
        return count

solu = Solution()
print solu.NumberOf12(3)
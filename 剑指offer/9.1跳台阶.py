# -*- coding:utf-8 -*-
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        fib1 = 1
        fib2 = 2
        fibn = 0
        for i in range(number - 2):
            fibn = fib1 + fib2
            fib1 = fib2
            fib2 = fibn
        return fibn

solu = Solution()
print solu.jumpFloor(5)
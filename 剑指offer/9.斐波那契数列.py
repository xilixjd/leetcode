# -*- coding:utf-8 -*-
'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''
class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        fib1 = 0
        fib2 = 1
        fibn = 0
        for i in range(n - 1):
            fibn = fib1 + fib2
            fib1 = fib2
            fib2 = fibn
        return fibn

solu = Solution()
print solu.Fibonacci(5)
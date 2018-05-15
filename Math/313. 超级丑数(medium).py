# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
编写一段程序来寻找第 n 个超级丑数。

超级丑数是指其所有质因数都在长度为k的质数列表primes中的正整数。
例如，[1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]，
是给定长度为 4 的质数列表primes = [2, 7, 13, 19]的前 12 个超级丑数。

注意:
(1) 1是任何给定的primes的超级丑数。
(2) 给定primes中的数字以升序排列。
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
(4) 第n个超级丑数可以认为在32位有符整数的表示范围内。
'''


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        def find_min(primes_point, primes, stack):
            primes_array = [primes[i] * stack[primes_point[i]] for i in range(len(primes))]
            return primes_array

        stack = [1]
        primes_point = [0 for i in range(len(primes))]
        while len(stack) < n:
            primes_array = find_min(primes_point, primes, stack)
            min_ugly = min(primes_array)
            stack.append(min_ugly)
            for i in range(len(primes)):
                if stack[primes_point[i]] * primes[i] == min_ugly:
                    primes_point[i] += 1
        return stack[-1]

solu = Solution()
print solu.nthSuperUglyNumber(12, [2, 7, 13, 19])
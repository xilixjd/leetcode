# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Description:

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count


    def isPrime(self, m):
        '''
        超时
        :param m:
        :return:
        '''
        if m == 1:
            return False
        i = 2
        while i*i <= m:
            if m % i == 0:
                return False
            i += 1
        return True

    def countPrimesFasr(self, n):
        if n == 0 or n == 1:
            return 0
        count = 0
        array = [0 for i in range(n+1)]
        for i in range(2, len(array)):
            if array[i] == 0:
                count += 1
                j = 2
                while i * j < n:
                    array[i * j] = 1
                    j += 1
        return count

solu = Solution()
print solu.countPrimesFasr(2)
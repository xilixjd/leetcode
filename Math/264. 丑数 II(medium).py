# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''


class Solution(object):
    def nthUglyNumber2(self, n):
        '''
        超时
        :param n:
        :return:
        '''
        def isUgly(num):
            """
            :type num: int
            :rtype: bool
            """
            if num <= 0:
                return False
            while num % 2 == 0:
                num /= 2
            while num % 3 == 0:
                num /= 3
            while num % 5 == 0:
                num /= 5
            return True if num == 1 else False

        count = 1
        i = 2

        while count < n:
            while not isUgly(i):
                i += 1
            count += 1
            i += 1
        return i - 1

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 占用空间太大
        # if n == 1:
        #     return 1
        # array = [None for i in range(1690 * 500 + 1)]
        # array[1] = 1
        # array[2] = 1
        # array[3] = 1
        # array[5] = 1
        # count = 1
        # for i in range(2, len(array)):
        #     if array[i] == 1:
        #         count += 1
        #         print count, i
        #         if count == n:
        #             return i
        #         l = k = j = i
        #         while j < 1690 * 500:
        #             array[j] = 1
        #             j *= 2
        #         while k < 1690 * 500:
        #             array[k] = 1
        #             k *= 3
        #         while l < 1690 * 500:
        #             array[l] = 1
        #             l *= 5
        # print array


        stack = [1]
        i = k = j = 0
        while len(stack) < n:
            stack.append(min(stack[i] * 2, min(stack[j] * 3, stack[k] * 5)))
            if stack[-1] == stack[i] * 2:
                i += 1
            if stack[-1] == stack[j] * 3:
                j += 1
            if stack[-1] == stack[k] * 5:
                k += 1
        return stack[-1]




solu = Solution()
print solu.nthUglyNumber(1500)
print solu.nthUglyNumber2(1500)
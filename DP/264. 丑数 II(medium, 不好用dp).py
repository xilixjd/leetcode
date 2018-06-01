# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前10个丑数。
说明:  

1 是丑数。
n 不超过1690。
'''


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = j = k = 0
        stack = [1]
        while len(stack) < n:
            next_ugly = min(min(stack[i] * 2, stack[j] * 3), stack[k] * 5)
            if next_ugly == stack[i] * 2:
                i += 1
            if next_ugly == stack[j] * 3:
                j += 1
            if next_ugly == stack[k] * 5:
                k += 1
            stack.append(next_ugly)
        return stack[-1]

solu = Solution()
print solu.nthUglyNumber(10)
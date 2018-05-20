# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:

n = 5

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤

因为第三行不完整，所以返回2.
示例 2:

n = 8

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

因为第四行不完整，所以返回3.
'''


class Solution(object):
    def arrangeCoins(self, n):
        """
        递归会爆栈
        :type n: int
        :rtype: int
        """
        def helper(n, remain, count):
            # print remain, count
            if remain < count + 1:
                return count
            else:
                count += 1
            return helper(n, remain - count, count)

        return helper(n, n, 0)

    def arrangeCoins2(self, n):
        if n == 0:
            return 0
        count = 1
        while n > count:
            n -= count
            count += 1
        return count if count == n else count - 1

solu = Solution()
print solu.arrangeCoins2(1)
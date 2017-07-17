# -*- coding:utf-8 -*-
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
class Solution:
    def reOrderArray(self, array):
        p1 = 0
        p2 = len(array) - 1
        while p1 < p2:
            while p1 < p2 and self.isOdd(array[p1]):
                p1 += 1
            while p1 < p2 and not self.isOdd(array[p2]):
                p2 -= 1
            if p1 < p2:
                array[p1], array[p2] = array[p2], array[p1]
        return array

    def isOdd(self, n):
        return (n & 1) == 1

solu = Solution()
print solu.reOrderArray([1, 2, 3, 4, 5, 6])
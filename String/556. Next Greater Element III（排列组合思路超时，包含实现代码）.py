# -*- coding: utf-8 -*-
'''
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly 
the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, 
you need to return -1.

Example 1:
Input: 12
Output: 21
Example 2:
Input: 21
Output: -1
'''
import itertools

class Solution(object):
    def nextGreaterElementMy(self, n):
        """
        超时
        :type n: int
        :rtype: int
        """
        str_n = str(n)
        arrange_str_n = itertools.permutations(str_n, len(str_n))
        arrange_str_n = list(set(arrange_str_n))
        array_str_n = [int(''.join(i)) for i in arrange_str_n]
        min_num = max(array_str_n)
        if min_num == n:
            return -1
        for i in range(len(array_str_n)):
            if array_str_n[i] > n:
                min_num = min(min_num, array_str_n[i])
                
        return min_num

    def nextGreaterElementFast(self, n):
        '''
        以 12452 举例，从后往前，52 递减，则将递减的 reverse ，变成 12425
        第一个不递减的数 4,将 4 替换为 大于 4 的数且正在递减的数即 5 变成 12524
        '''
        str_n = list(str(n))
        if len(str_n) == 2:
            if int(''.join(str_n)) >= int(''.join(str_n[::-1])):
                return -1
            else:
                return int(''.join(str_n[::-1]))
        for i in range(len(str_n))[::-1]:
            if str_n[i-1] == str_n[i]:
                continue
            if str_n[i-1] < str_n[i]:
                break
        # print i
        if i == 0:
            return -1
        str_n[i:] = str_n[i:][::-1]
        # print str_n
        for j in range(i, len(str_n)):
            if int(str_n[j]) > int(str_n[i-1]):
                str_n[j], str_n[i-1] = str_n[i-1], str_n[j]
                break
        if len(str_n) == 10:
            return -1
        return int(''.join(str_n))
                


    def permute(self, num):
        '''
        排列组合实现
        '''
        if len(num) == 0: return []
        if len(num) == 1: return [num]
        res = []
        for i in range(len(num)):
            for j in self.permute(num[:i] + num[i+1:]):
                res.append([num[i]] + j)
        return res

solu = Solution()
print solu.nextGreaterElementFast(1999999999)
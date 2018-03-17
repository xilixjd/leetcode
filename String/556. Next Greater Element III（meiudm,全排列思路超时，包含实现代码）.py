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


class ReSolution(object):
    def nextGreaterElement1(self, n):
        """
        思路1：
        全排列，超时
        :type n: int
        :rtype: int
        """
        def permute(nums):
            if len(nums) == 0:
                return []
            if len(nums) == 1:
                return [nums]
            res = []
            for i in range(len(nums)):
                for j in permute(nums[:i] + nums[i + 1:]):
                    res.append([nums[i]] + j)
            return res
        str_num = str(n)
        permute_array = [int(''.join(p)) for p in permute(list(str_num))]
        max_num = max(permute_array)
        if max_num == n:
            return -1
        permute_array = list(set(permute_array))
        permute_array = sorted(permute_array)
        print permute_array
        return permute_array[permute_array.index(n) + 1]

    def nextGreaterElement2(self, n):
        """
        思路2：
        全排列，超时
        :type n: int
        :rtype: int
        """
        def find_bigger_num_not_equal(s, i):
            '''
            找到一个比 s[i] 刚好大一点的数
            :param s:
            :param i:
            :return:
            '''
            bigger_num = max(s[i + 1:])
            index = i
            for j in range(i + 1, len(s)):
                if s[j] > s[i]:
                    if s[j] <= bigger_num:
                        bigger_num = s[j]
                        index = j
            return index
        def sort_array(array, i):
            return array[:i + 1] + sorted(array[i + 1:])
        if len(str(n)) == 1:
            return -1
        if len(str(n)) == 2:
            if n >= int(str(n)[::-1]):
                return -1
            else:
                return int(str(n)[::-1])
        def last_increase_array(array):
            index = -1
            for i in range(len(array) - 1):
                if array[i + 1] > array[i]:
                    index = i
            return index
        array_n = [int(c) for c in list(str(n))]
        if len(array_n) >= 10:
            return -1
        index = last_increase_array(array_n)
        if index == -1:
            return -1
        smaller_index = find_bigger_num_not_equal(array_n, index)
        print index, smaller_index
        array_n[index], array_n[smaller_index] = array_n[smaller_index], array_n[index]
        array_n = sort_array(array_n, index)
        res = int(''.join(str(c) for c in array_n))
        return res


re = ReSolution()
print re.nextGreaterElement2(199999)


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
# print solu.nextGreaterElementFast(1999999999)
# print solu.permute(["a", "b", "c", "d"])
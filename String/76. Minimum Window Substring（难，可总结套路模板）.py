# -*- coding: utf-8 -*-
'''
Given a string S and a string T, find the minimum window in S
which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows,
you are guaranteed that there will always be only one unique minimum window in S.
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        套路，模板：
        https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems
        :type s: str
        :type t: str
        :rtype: str
        [0,10],[5,12],[3,9] => [0,5,3],[0,5,9],[0,12,3],[0,12,9] 的算法怎么求？

        for j in range(len(array[0])):
            temp_array = [array[0][j]]
            for k in range(len(array[1])):
                if len(temp_array) == 2:
                    temp_array.pop()
                temp_array.append(array[1][k])
                for l in range(len(array[2])):
                    temp_array.append(array[2][l])
                    temp_array1 = copy.deepcopy(temp_array)
                    result.append(temp_array1)
                    temp_array.pop()
        """
        m = len(s)
        n = len(t)
        if m < n:
            return ""
        lt = {}
        for i in t:
            if i not in lt:
                lt[i] = 1
            else:
                lt[i] += 1
        missing = n
        i = I = J = 0
        for j, c in enumerate(s, 1):
            if c in lt and lt[c] > 0:
                missing -= 1
            if c in lt:
                lt[c] -= 1
            while i < j and not missing:
                if not J or j - i < J - I:
                    I, J = i, j
                if s[i] not in lt:
                    i += 1
                else:
                    lt[s[i]] += 1
                    if lt[s[i]] > 0:
                        missing += 1
                    i += 1
        return s[I: J]

solu = Solution()
print solu.minWindow('ADOBECODEBANC', 'ABC')
# -*- coding: utf-8 -*-
'''
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
'''

class Solution(object):
    def nearestPalindromicFast(self, S):
        K = len(S)
        candidates = [str(10 ** k + d) for k in (K - 1, K) for d in (-1, 1)]
        print candidates
        prefix = S[:(K + 1) / 2]
        P = int(prefix)
        for start in map(str, (P - 1, P, P + 1)):
            candidates.append(start + (start[:-1] if K % 2 else start)[::-1])
        print candidates

        def delta(x):
            return abs(int(S) - int(x))

        ans = None
        for cand in candidates:
            if cand != S and not cand.startswith('00'):
                if (ans is None or delta(cand) < delta(ans) or
                                delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand
        return ans

    def nearestPalindromic(self, n):
        """
        此题关键在于不能等于自己
        :type n: str
        :rtype: str
        """
        if len(n) == 1:
            return str(int(n) - 1)
        candidate = []
        candidate.append(str(10 ** (len(n) - 1) - 1))
        candidate.append(str(10 ** len(n) + 1))
        candidate.append(self.make_palindromic(n))
        # 加 1 再转回文
        # candidate.append(self.make_palindromic(self.changeMidPlus1(n)))
        # candidate.append(self.make_palindromic(self.changeMidMinus1(n)))
        prefix = n[:(len(n) + 1) / 2]
        P = int(prefix)
        for start in map(str, (P - 1, P + 1)):
            candidate.append(start + (start[:-1] if len(n) % 2 else start)[::-1])
        print candidate
        diff = 10000000000000
        mark = 0
        for i in range(len(candidate)):
            temp = self.get_diff(candidate[i], n)
            if temp > 0 and temp < diff:
                mark = i
                diff = temp
            elif temp > 0 and temp == diff:
                if int(candidate[i]) < int(candidate[mark]):
                    mark = i
        return candidate[mark]

    def make_palindromic(self, n):
        len_n = len(n)
        mid = len_n / 2
        j = mid - 1
        array = list(n)
        if len_n % 2 != 0:
            mid += 1
            j = mid - 2
        for i in range(mid, len(array)):
            array[i] = array[j]
            j -= 1
        return "".join(array)

    def changeMidPlus1(self, n):
        a = list(n)
        mid = (len(n) - 1) / 2
        a[mid] = str(int(a[mid]) + 1)
        return "".join(a)

    def changeMidMinus1(self, n):
        a = list(n)
        mid = (len(n) - 1) / 2
        a[mid] = str(int(a[mid]) - 1)
        return "".join(a)

    def get_diff(self, s, n):
        return abs(int(s) - int(n))

solu = Solution()
print solu.nearestPalindromic('100')

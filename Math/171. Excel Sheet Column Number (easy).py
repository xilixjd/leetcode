
'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
Credits:
Special thanks to @ts for adding this problem and creating all test cases.


'''


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        trans_dict = {}
        j = 0
        for i in range(65, 91):
            trans_dict[chr(i)] = j + 1
            j += 1
        total = 0
        j = 0
        for i in range(len(s) - 1, -1, -1):
            total += trans_dict[s[i]] * pow(26, j)
            j += 1
        return total

solu = Solution()
print solu.titleToNumber('')
# -*- coding: utf-8 -*-

'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''


class ReSolution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        temp_array = [1, 1]
        for i in range(rowIndex - 2):
            mid_array = []
            for j in range(len(temp_array) - 1):
                mid_array.append(temp_array[j] + temp_array[j + 1])
            temp_array = [1] + mid_array + [1]
        return temp_array

re = ReSolution()
print re.getRow(1)


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(rowIndex):
            row.insert(0, 1)
            for j in range(1, len(row) - 1):
                row[j] = row[j] + row[j + 1]
        return row

solu = Solution()
# print solu.getRow(3)
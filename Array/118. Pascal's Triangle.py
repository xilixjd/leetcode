# -*- coding: utf-8 -*-

'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        temp_array = [1, 1]
        for n in range(3, numRows + 1):
            mid_array = []
            for i in range(len(temp_array) - 1):
                mid_array.append(temp_array[i] + temp_array[i + 1])
            mid_array.insert(0, 1)
            mid_array.append(1)
            res.append(mid_array)
            temp_array = mid_array
        return res

    def generate2(self, numRows):
        import copy
        allrows = []
        row = []
        for i in range(numRows):
            row.insert(0, 1)
            for j in range(1, len(row) - 1):
                row[j] = row[j] + row[j + 1]
            # 这里有个 Python 比较坑的问题是 按引用传递
            # a = [1, 2], b = [3, 4]
            # a.append(b) # a: [1, 2, [3, 4]]
            # b[1] = 5 # a: [1, 2, [3, 5]]
            temp = copy.deepcopy(row)
            allrows.append(temp)
            print allrows
        return allrows

solu = Solution()
print solu.generate2(9)

# -*- coding: utf-8 -*-

'''
Given a 2D binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
'''


class ReSolution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def calc_area(nums):
            stack = []
            res = 0
            for i in range(len(nums)):
                if len(stack) == 0 or nums[i] >= stack[-1]:
                    stack.append(nums[i])
                else:
                    count = 0
                    while len(stack) != 0 and nums[i] < stack[-1]:
                        count += 1
                        res = max(res, stack[-1] * count)
                        stack.pop()
                    while count > 0:
                        stack.append(nums[i])
                        count -= 1
                    stack.append(nums[i])
            count = 0
            while len(stack) != 0:
                count += 1
                res = max(res, stack[-1] * count)
                stack.pop()
            return res

        if len(matrix) == 0:
            return 0
        heights = [0 for i in range(len(matrix[0]))]
        area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heights[j] = 0 if int(matrix[i][j]) == 0 else heights[j] + 1
            area = max(area, calc_area(heights))
        return area

re = ReSolution()
# print re.maximalRectangle([["1","0","1","0","0"],
#                            ["1","0","1","1","1"],
#                            ["1","1","1","1","1"],
#                            ["1","0","0","1","0"]])


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        思路：从上到下遍历每行，记录 heights[]
        如果 matrix[i][j] == 1,则 heights[j] += 1
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        heights = [0 for i in matrix[0]]
        area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heights[j] = 0 if int(matrix[i][j]) == 0 else heights[j] + 1
            area = max(area, self.largestRectangleArea(heights))
        return area

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        res = 0
        for i in range(len(heights)):
            if len(stack) == 0 or stack[-1] <= heights[i]:
                stack.append(heights[i])
            else:
                count = 0
                while len(stack) != 0 and stack[-1] > heights[i]:
                    count += 1
                    res = max(res, count * stack[-1])
                    stack.pop()
                while count > 0:
                    stack.append(heights[i])
                    count -= 1
                stack.append(heights[i])
        count = 1
        while len(stack) > 0:
            res = max(res, count * stack[-1])
            stack.pop()
            count += 1
        return res



    def maximalRectangle2(self, matrix):
        '''
        DP
        通过计算左右边界及高度来获取最大面积

        ["10100","10111","11111","10010"] 报错，没去研究了
        :param matrix:
        :return:
        '''
        if len(matrix) == 0:
            return 0
        heights = [0 for i in matrix[0]]
        left = [0 for i in matrix[0]]
        right = [len(matrix[0]) for i in matrix[0]]
        m = len(matrix)
        n = len(matrix[0])
        max_area = 0
        for i in range(m):
            cur_left = 0
            cur_right = n
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            for k in range(n):
                if matrix[i][k] == '1':
                    left[k] = max(cur_left, left[k])
                else:
                    left[k] = 0
                    cur_left = k + 1
            for l in range(n)[::-1]:
                if matrix[i][l] == '1':
                    right[l] = min(cur_right, right[l])
                else:
                    right[l] = n
                    cur_right = l
            # print i
            print left
            print right
            for h in range(n):
                max_area = max(max_area, (right[h] - left[h]) * heights[h])
        return max_area


solu = Solution()
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# print solu.maximalRectangle([
#     "0001000",
#     "0010100",
#     "0101100",
# ])
print solu.maximalRectangle2(["10100",
                              "10111",
                              "11111",
                              "10010"])
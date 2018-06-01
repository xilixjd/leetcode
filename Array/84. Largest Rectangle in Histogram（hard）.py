# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/largest-rectangle-in-histogram/#/description

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
'''


class ReSolution(object):
    def largestRectangleArea(self, heights):
        stack = []
        res = 0
        for i in range(len(heights)):
            if len(stack) == 0 or heights[i] >= stack[-1]:
                stack.append(heights[i])
            else:
                count = 0
                while len(stack) != 0 and heights[i] < stack[-1]:
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
            count += 1
            stack.pop()
        return res


solu = ReSolution()
print solu.largestRectangleArea([2,1,5,6,2,3,4])


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        思路1：遍历每个柱子，分别向左边与右边搜索，遇到比当前柱子更矮的就停止，记录面积
        这样效率太低，通不过

        思路2：利用 stack 如 heights: [2,1,5,6,2,3]
        遍历 heights，栈为空或者栈顶元素比 heights[i] 小，则将 heights[i] 进栈
        否则，出栈并重新将元素进栈，进栈元素替换为 heights[i]

        （1）2进栈。s={2}, result = 0

        （2）1比2小，不满足升序条件，因此将2弹出，并记录当前结果为2*1=2。

        将2替换为1重新进栈。s={1,1}, result = 2

        （3）5比1大，满足升序条件，进栈。s={1,1,5},result = 2

        （4）6比5大，满足升序条件，进栈。s={1,1,5,6},result = 2

        （5）2比6小，不满足升序条件，因此将6弹出，并记录当前结果为6*1=6。s={1,1,5},result = 6

        2比5小，不满足升序条件，因此将5弹出，并记录当前结果为5*2=10
        （因为已经弹出的5,6是升序的）。s={1,1},result = 10

        2比1大，将弹出的5,6替换为2重新进栈。s={1,1,2,2,2},result = 10

        （6）3比2大，满足升序条件，进栈。s={1,1,2,2,2,3},result = 10

        栈构建完成，满足升序条件，因此按照升序处理办法得到上述的
        max(height[i]*(size-i))=max{3*1, 2*2, 2*3, 2*4, 1*5, 1*6}=8<10

        综上所述，result=10

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


# solu = Solution()
# print solu.largestRectangleArea([2,1,5,6,2,3,4])
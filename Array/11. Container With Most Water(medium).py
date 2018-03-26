# -*- coding: utf-8 -*-
'''
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''


class ReSolution(object):
    def maxAreaMy(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_countainer = 0
        while i < j:
            min_h = min(height[i], height[j])
            max_countainer = max(max_countainer, min_h * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_countainer

re = ReSolution()
print re.maxAreaMy([5,4,3,2,4])

class Solution(object):
    def maxAreaMy(self, height):
        """
        :type height: List[int]
        :rtype: int
        超时 ！！！ 40/49
        """
        height_dict = {}
        max_countain = -1
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                width = j - i
                countain = width * min(height[i], height[j])
                max_countain = max(max_countain, countain)
        return max_countain

    def maxAreaFast(self, height):
        i = 0
        j = len(height) - 1
        max_cou = 0
        while i < j:
            h = min(height[i], height[j])
            max_cou = max((j - i) * h, max_cou)
            while i < j and height[i] <= h:
                i += 1
            while i < j and height[j] <= h:
                j -= 1
        return max_cou

    def maxAreaFaster(self, height):
        i = 0
        j = len(height) - 1
        max_cou = 0
        while i < j:
            h = min(height[i], height[j])
            max_cou = max((j - i) * h, max_cou)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_cou

    def maxAreaMy2(self, height):
        maxArea = -1000
        i = 0
        j = len(height) - 1
        while i < j:
            h = min(height[i], height[j])
            area = h * (j - i)
            maxArea = max(area, maxArea)
            while i < j and height[i] <= h:
                i += 1
            while i < j and height[j] <= h:
                j -= 1
        return maxArea


solu = Solution()
print solu.maxAreaMy2([5,4,3,2,4])
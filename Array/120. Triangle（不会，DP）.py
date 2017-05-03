# -*- coding: utf-8 -*-
'''
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        从下到上 DP
        :type triangle: List[List[int]]
        :rtype: int
        """
        sums = [0 for i in range(len(triangle) + 1)]
        for i in range(0, len(triangle))[::-1]:
            for j in range(i + 1):
                sums[j] = min(sums[j], sums[j+1]) + triangle[i][j]
        return sums[0]

    def minimumTotal1(self, triangle):
        '''
        非 DP 方法
        较好理解
        从上到下，改变 triangle 的方法，
        依次从上往下，每个节点的值累加计算，最后算最后一行中最小的数
        :param triangle:
        :return:
        '''
        clist = triangle[0]
        for i in range(len(triangle) - 1):
            nlist = triangle[i + 1]
            nlist[0] = nlist[0] + clist[0]
            for j in range(1, len(nlist) - 1):
                nlist[j] = nlist[j] + min(clist[j], clist[j - 1])
            nlist[i + 1] = nlist[i + 1] + clist[i]
            clist = nlist
        min_sum = clist[0]
        for c in clist:
            min_sum = min(min_sum, c)
        return min_sum

    def minimumTotal1DP(self, triangle):
        '''
        根据上个方法衍生的 DP 方法，把空间复杂度降低为 O(n)
        :param triangle:
        :return:
        '''
        pathInfo = [0 for i in range(len(triangle))]
        pathInfo[0] = triangle[0][0]
        # 从第二层开始
        for i in range(1, len(triangle)):
            for j in range(0, i + 1)[::-1]:
                if j == len(triangle[i]) - 1:
                    pathInfo[j] = pathInfo[j - 1] + triangle[i][j]
                elif j == 0:
                    pathInfo[j] = pathInfo[j] + triangle[i][j]
                else:
                    pathInfo[j] = min(pathInfo[j], pathInfo[j - 1]) + triangle[i][j]
        min_sum = pathInfo[0]
        for p in pathInfo:
            min_sum = min(p, min_sum)
        return min_sum



solu = Solution()
print solu.minimumTotal([[-1],[2,3],[1,-1,-3]])
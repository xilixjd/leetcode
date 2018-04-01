# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        https://leetcode.com/problems/merge-intervals/discuss/21222/A-simple-Java-solution
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda k: k.start)
        start = intervals[0].start
        end = intervals[0].end
        merge_array = []
        for inter in intervals:
            if inter.start <= end:
                end = max(inter.end, end)
            else:
                merge_array.append(Interval(start, end))
                start = inter.start
                end = inter.end
        merge_array.append(Interval(start, end))
        return merge_array


solu = Solution()
print solu.merge([Interval(2, 6), Interval(1, 3), Interval(8, 10), Interval(9, 11)])

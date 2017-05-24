# -*- coding: utf-8 -*-

'''
Given a list of 24-hour clock time points in "Hour:Minutes" format, 
find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
'''

class Solution(object):
    def findMinDifference(self, timePoints):
        buckets = [False for i in range(60 * 24)]
        for i in range(len(timePoints)):
            hour = int(timePoints[i].split(':')[0])
            minute = int(timePoints[i].split(':')[1])
            if buckets[hour*60 + minute]:
                return 0
            buckets[hour*60+minute] = True
        first = 200000
        last = -1
        min_min = 200000
        prev = 0
        for i in range(60*24):
            if buckets[i]:
                if first != 200000:
                    min_min = min(min_min, i - prev)
                last = max(last, i)
                first = min(first, i)
                prev = i
        return min(min_min, 60*24 - last + first)

            

    def findMinDifferenceMy(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        超时
        """
        min_min = 200000
        if len(timePoints) < 2:
            return 0
        for i in range(len(timePoints)):
            for j in range(i + 1, len(timePoints)):
                min_min = min(min_min, self.findMinBetweenTwo(timePoints[i], timePoints[j]))
        return min_min

    
    def findMinBetweenTwo(self, time1_str, time2_str):
        time1_hour = int(time1_str.split(':')[0])
        time1_min = int(time1_str.split(':')[1])
        time2_hour = int(time2_str.split(':')[0])
        time2_min = int(time2_str.split(':')[1])
        if time1_hour > time2_hour:
            time1_diff1 = 60 * (24 - time1_hour - 1) + 60 - time1_min + time2_hour * 60 + time2_min
            if time1_min >= time2_min:
                time1_diff2 = 60 * (time1_hour - time2_hour) + time1_min - time2_min
            else:
                time1_diff2 = 60 * (time1_hour - time2_hour - 1) + time1_min - time2_min + 60
            time_diff = min(abs(time1_diff1), abs(time1_diff2))
        else:
            time1_diff1 = 60 * (24 - time2_hour - 1) + 60 - time2_min + time1_hour * 60 + time1_min
            if time2_min >= time1_min:
                time1_diff2 = 60 * (time2_hour - time1_hour) + time2_min - time1_min
            else:
                time1_diff2 = 60 * (time2_hour - time1_hour - 1) + time2_min - time1_min + 60
            time_diff = min(abs(time1_diff1), abs(time1_diff2))
        return time_diff
        # time1_diff2 = 


solu = Solution()
print solu.findMinDifferenceMy(['00:40', '23:59', '00:00'])

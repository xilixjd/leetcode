# -*- coding:utf-8 -*-
# 二分查找

class Solution:
    def BinarySearch(self, array, target):
        n = len(array)
        if n == 0:
            return -1
        start = 0
        end = n - 1
        while start + 1 < end:
            mid = int((start + end) / 2)
            if array[mid] == target:
                start = mid
            elif array[mid] < target:
                start = mid
            else:
                end = mid

        if array[start] == target:
            return start
        if array[end] == target:
            return end

        return -1


if __name__ == '__main__':
    a = [1, 3, 4, 5, 6, 7, 34]
    s = Solution()
    print(s.BinarySearch(a, 5))
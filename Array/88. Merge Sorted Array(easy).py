# -*- coding: utf-8 -*-
'''
Total Accepted: 156896
Total Submissions: 494118
Difficulty: Easy
Contributor: LeetCode
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
'''


class ReSolution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1


re = ReSolution()
print re.merge([4,5,6,0,0,0],3,[1,2,3],3)


class Solution(object):
    def mergeMy(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums_temp = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums_temp.append(nums1[i])
                i += 1
            else:
                nums_temp.append(nums2[j])
                j += 1
        if m != 0:
            nums_temp += nums1[i:]
        if n != 0:
            nums_temp += nums2[j:]
        nums1 = nums_temp
        print nums1

    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

    def mergeMy2(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:m] = nums2[:n]

solu = Solution()
print solu.mergeMy2([1, 0], 1, [2], 1)
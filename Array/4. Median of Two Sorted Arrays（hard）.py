# -*- coding: utf-8 -*-
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution(object):
    def findMedianSortedArraysMy(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        时间复杂度不满足
        """
        i = j = 0
        nums = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        nums += nums1[i:]
        nums += nums2[j:]
        if len(nums) % 2:
            return (nums[len(nums) / 2])
        else:
            return float(nums[len(nums) / 2] + nums[len(nums) / 2 - 1]) / 2

solu = Solution()
print solu.findMedianSortedArraysMy([1, 3], [2, 4])

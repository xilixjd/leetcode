# -*- coding: utf-8 -*-

'''
Find the contiguous subarray within an array
(containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''


class ReSolution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = iMax = iMin = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                iMax, iMin = iMin, iMax
            iMax = max(nums[i], nums[i] * iMax)
            iMin = min(nums[i], nums[i] * iMin)
            res = max(res, iMax)
        return res


    def maxProduct2(self, nums):
        """
        https://leetcode.com/problems/maximum-product-subarray/discuss/48330/Simple-Java-code
        更好理解
        :type nums: List[int]
        :rtype: int
        """
        res = iMax = iMin = nums[0]
        for i in range(1, len(nums)):
            temp = iMax
            iMax = max(max(nums[i] * iMax, nums[i] * iMin), nums[i])
            iMin = min(min(nums[i] * iMin, nums[i] * temp), nums[i])
            res = max(res, iMax)
        return res


re = ReSolution()
print re.maxProduct([2,3,-2,4])


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        imax = nums[0]
        imin = nums[0]
        r = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])
            r = max(r, imax)
        return r

    def maxProductMy(self, nums):
        if len(nums) == 0:
            return
        r = iMax = iMin = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                iMax, iMin = iMin, iMax
            iMax = max(nums[i], nums[i] * iMax)
            iMin = min(nums[i], nums[i] * iMin)
            r = max(r, iMax)
        return r



solu = Solution()
print solu.maxProductMy([3, 4, -0.1, 7, 8])
# -*- coding: utf-8 -*-

'''
Find the contiguous subarray within an array
(containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_product = nums[0]
        # temp = 1
        # for n in nums:
        #     if temp * n >= max_product:
        #         max_product = temp * n
        #         temp = temp * n
        #         if nums[0] == 0:
        #             temp = 1
        #     elif n >= max_product:
        #         max_product = n
        #         temp = n
        #     else:
        #         if n <= 0:
        #             temp = 1
        #         else:
        #             temp = n
        # return max_product


solu = Solution()
print solu.maxProduct([-2,3,-4])
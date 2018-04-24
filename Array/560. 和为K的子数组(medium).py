# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

'''


class Solution(object):
    def subarraySum(self, nums, k):
        """
        暴力法——肯定超时
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # count = 0
        # for i in range(len(nums)):
        #     sums = 0
        #     for j in range(i, len(nums)):
        #         sums += nums[j]
        #         if sums == k:
        #             count += 1
        # return count

        count = 0
        sum_array = [0 for i in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            sum_array[i] = sum_array[i - 1] + nums[i - 1]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if sum_array[j] - sum_array[i] == k:
                    count += 1
        return count

    def subarraySum2(self, nums, k):
        '''
        https://leetcode.com/problems/subarray-sum-equals-k/solution/
        :param nums:
        :param k:
        :return:
        '''
        pre_sum_dict = {0: 1}
        count = 0
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if pre_sum_dict.get(sums - k) is not None:
                count += pre_sum_dict.get(sums - k)
            pre_sum_dict[sums] = pre_sum_dict.get(sums, 0) + 1
        return count


solu = Solution()
print solu.subarraySum2([3,4,7,2,-3,1,4,2,1], 7)
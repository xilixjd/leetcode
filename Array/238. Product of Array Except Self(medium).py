# -*- coding: utf-8 -*-
'''
Given an array of n integers where n > 1, nums,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
'''


class ReSolution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp_array = []
        temp = 1
        for i in range(len(nums)):
            temp_array.append(temp)
            temp *= nums[i]
        temp = 1
        for i in range(len(nums))[::-1]:
            temp_array[i] *= temp
            temp *= nums[i]
        return temp_array


re = ReSolution()
print re.productExceptSelf([1,2,3,4])


class Solution(object):
    def productExceptSelfMy(self, nums):
        """
        暴力解法
        :type nums: List[int]
        :rtype: List[int]
        """
        temp_nums = []
        for i in range(len(nums)):
            count = 1
            for j in range(len(nums)):
                if i != j:
                    count *= nums[j]
            temp_nums.append(count)
        return temp_nums

    def productExceptSelf(self, nums):
        temp = 1
        temp_array = []
        for n in nums:
            temp_array.append(temp)
            temp *= n
        temp = 1
        for i in range(len(nums))[::-1]:
            temp_array[i] = temp * temp_array[i]
            temp *= nums[i]
        return temp_array

solu = Solution()
print solu.productExceptSelf([1,2,3,4])
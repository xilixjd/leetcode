# -*- coding: utf-8 -*-
'''
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''


class Solution(object):
    def moveZeroesMy(self, nums):
        """
        此方法不能排序 题目要求好像是非 0 的顺序也不能变
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0 and abs(j) <= len(nums) / 2:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        return nums

    def moveZeroes(self, nums):
        i = 0
        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1
        print nums
        while i < len(nums):
            nums[i] = 0
            i += 1
        return nums

    def moveZeroesFast(self, nums):
        i = 0
        # 遍历数组位数
        j = 0
        for n in nums:
            if n != 0:
                nums[i], nums[j] = n, nums[i]
                i += 1
            j += 1
        print nums



solu = Solution()
print solu.moveZeroesFast([0,0,1])
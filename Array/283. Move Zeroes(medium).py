# -*- coding: utf-8 -*-
'''
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''


class ReSolution(object):
    def moveZeroes(self, nums):
        """
        思路：
        将不为 0 的数与第一个为 0 且 index 大于这个不为 0 的数的 index 进行交换
        然而超时了
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 超时
        # def get_first_zero_index(nums):
        #     for i in range(len(nums)):
        #         if nums[i] == 0:
        #             return i
        #     return -1
        #
        # i = 0
        # while i < len(nums):
        #     if nums[i] != 0:
        #         zero_index = get_first_zero_index(nums)
        #         if zero_index == -1:
        #             break
        #         if zero_index > i:
        #             i += 1
        #             continue
        #         nums[i], nums[zero_index] = nums[zero_index], nums[i]
        #     i += 1
        # print nums

        # 可行
        # i = 0
        # array_zeros = []
        # length = len(nums)
        # while i < length:
        #
        #     if nums[i] == 0:
        #         nums.append(0)
        #         array_zeros.append(i)
        #     i += 1
        # count = 0
        # for z in array_zeros:
        #     del nums[z - count]
        #     count += 1


        count_zeros = i = 0
        for n in nums:
            if n == 0:
                count_zeros += 1
        while i < len(nums):
            if nums[i] == 0:
                if len(nums) - i <= count_zeros:
                    break
                del nums[i]
                nums.append(0)
            else:
                i += 1
        print nums

re = ReSolution()
re.moveZeroes([0,0,0,1])


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
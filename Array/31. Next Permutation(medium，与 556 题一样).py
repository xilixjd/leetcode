# -*- coding: utf-8 -*-
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

import random

class ReSolution(object):
    def nextPermutation(self, nums):
        """
        全排列法，不符合题意，且用时过长
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def permutation(nums):
            if len(nums) == 0:
                return ""
            if len(nums) == 1:
                return nums
            res = []
            for i in range(len(nums)):
                for j in permutation(nums[:i] + nums[i + 1:]):
                    res.append(nums[i] + j)
            return res

        nums_array = [str(n) for n in nums]
        nums_str = "".join(nums_array)
        permute_nums_str = permutation(nums_str)
        permute_nums = [int(p) for p in permute_nums_str]
        permute_nums.sort()
        index = permute_nums.index(int(nums_str))
        print permute_nums
        p_index = index + 1 if index != len(permute_nums) - 1 else 0
        return [int(p) for p in list(str(permute_nums[p_index]))]

    def nextPermutation1(self, nums):
        '''
        思路与 556 题一样
        :param nums:
        :return:
        '''
        def find_bigger_and_swap(nums, index):
            swap_index = index + 1
            sign = nums[index]
            bigger = nums[index + 1]
            for i in range(index + 1, len(nums)):
                if nums[i] > sign:
                    if nums[i] < bigger:
                        bigger = nums[i]
                        swap_index = i
            nums[swap_index], nums[index] = nums[index], nums[swap_index]

        def find_last_increase(nums):
            index = -1
            for i in range(len(nums) - 1):
                if nums[i + 1] > nums[i]:
                    index = i
            return index

        def partition(nums, start, end):
            index = random.randint(start, end)
            nums[index], nums[end] = nums[end], nums[index]
            small = start - 1
            for i in range(start, end):
                if nums[i] < nums[end]:
                    small += 1
                    if small != i:
                        nums[small], nums[i] = nums[i], nums[small]
            small += 1
            nums[small], nums[end] = nums[end], nums[small]
            return small

        def quickSort(nums, start, end):
            if start > end:
                return
            index = partition(nums, start, end)
            quickSort(nums, start, index - 1)
            quickSort(nums, index + 1, end)

        index = find_last_increase(nums)
        if index == -1:
            nums.reverse()
        find_bigger_and_swap(nums, index)
        quickSort(nums, index + 1, len(nums) - 1)
        print nums


re = ReSolution()
print re.nextPermutation1([1,3,2])



class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = len(nums) - 1
        while j > 0:
            if nums[j-1] < nums[j]:
                break
            j -= 1
        if j == 0:
            nums.reverse()
        elif j == len(nums) - 1:
            nums[j-1], nums[-1] = nums[-1], nums[j-1]
        else:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            # nums[j-1], nums[-1] = nums[-1], nums[j-1]
            for k in range(j + 1, len(nums))[::-1]:
                if nums[j] < nums[k] < nums[j-1]:
                    nums[k], nums[j-1] = nums[j-1], nums[k]
                    break
            l = j
            while l < len(nums):
                for m in range(l + 1, len(nums)):
                    min_num = self.checkMinInRest(nums, m)
                    if nums[min_num] < nums[l]:
                        nums[min_num], nums[l] = nums[l], nums[min_num]
                        break
                l += 1
        print nums

    def checkMinInRest(self, nums, k):
        '''
        获得最小数的 index
        如果没有则 return -1
        :param nums:
        :param k:
        :return:
        '''
        min_num = {
            'index': -1,
            'value': 1000000
        }
        for i in range(k, len(nums)):
            if nums[i] < min_num['value']:
                min_num['index'] = i
                min_num['value'] = nums[i]
        return min_num['index']

    def nextPermutationMy(self, nums):
        j = len(nums) - 1
        while j > 0:
            if nums[j] > nums[j-1]:
                break
            j -= 1
        if j == 0:
            nums.reverse()
        elif j == len(nums) - 1:
            nums[j], nums[j-1] = nums[j-1], nums[j]
        else:
            least_index = self.findLeastNumBeyondJ(nums, j)
            nums[j-1], nums[least_index] = nums[least_index], nums[j-1]
            self.quickSort(nums, j, len(nums) - 1)
        print nums


    def findLeastNumBeyondJ(self, nums, j):
        '''
        :param nums:
        :param j:
        :return:
        '''
        min_dict = {
            'min_diff': 1000000000,
            'index': 0
        }
        for i in range(j, len(nums)):
            diff = nums[i] - nums[j-1]
            if diff > 0:
                if diff < min_dict['min_diff']:
                    min_dict['min_diff'] = diff
                    min_dict['index'] = i
        return min_dict['index']

    def partition(self, nums, start, end):
        index = random.randint(start, end)
        nums[index], nums[end] = nums[end], nums[index]
        small = start - 1
        for i in range(start, end):
            if nums[i] < nums[end]:
                small += 1
                if small != i:
                    nums[small], nums[i] = nums[i], nums[small]
        small += 1
        nums[small], nums[end] = nums[end], nums[small]
        return small

    def quickSort(self, nums, start, end):
        if start > end:
            return
        index = self.partition(nums, start, end)
        self.quickSort(nums, start, index - 1)
        self.quickSort(nums, index + 1, end)

    # def reverse_nums(self, nums, l, r):
    #     while l < r:
    #         print l, r
    #         nums[l], nums[r] = nums[r], nums[l]
    #         l += 1
    #         r -= 1


solu = Solution()
# solu.nextPermutationMy([5,4,7,5,3,2])
# solu.nextPermutationMy([1,3,2])
#[5,5,2,3,4,7]
# -*- coding: utf-8 -*-

# partition 算法

import random
class Solution():
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

    def mergeSortedArray(self, array_a, array_b):
        array = []
        i = j = 0
        while i < len(array_a) and j < len(array_b):
            if array_a[i] < array_b[j]:
                array.append(array_a[i])
                i += 1
            else:
                array.append(array_b[j])
                j += 1
        array += array_a[i:]
        array += array_b[j:]
        return array

    def mergeSort(self, array):
        length = len(array)
        if length <= 1:
            return array
        mid = length / 2
        left = self.mergeSort(array[:mid])
        right = self.mergeSort(array[mid:])
        return self.mergeSortedArray(left, right)

array = [3, 2, 1, 5, 4, 9, 7]
solu = Solution()
# print solu.quickSort(array, 0, len(array) - 1)
# print array
print solu.mergeSort(array)
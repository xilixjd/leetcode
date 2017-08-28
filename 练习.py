# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import random
class Solution():

# ==========================快速排序 quicksort===========================================================
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
# =====================================================================================

# ==========================归并排序 mergesort===========================================================
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
# =====================================================================================

# ==============================重建二叉树=======================================================
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0 or len(tin) == 0:
            return None
        inorderMap = {}
        for i in range(len(tin)):
            inorderMap[tin[i]] = i
        return self.construct(0, len(pre) - 1, pre, 0, len(tin) - 1, tin, inorderMap)

    def construct(self, prel, prer, pre, inl, inr, tin, inorderMap):
        if prel > prer or inl > inr:
            return
        root = TreeNode(pre[prel])
        preIndex = inorderMap[pre[prel]]
        root.left = self.construct(prel + 1, prel + preIndex - inl, pre, inl, preIndex - 1, tin, inorderMap)
        root.right = self.construct(prel + preIndex - inl + 1, prer, pre, preIndex + 1, inr, tin, inorderMap)
        return root
# =====================================================================================

    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

array = [3, 2, 1, 5, 4, 9, 7]
array.sort()
solu = Solution()
# print solu.quickSort(array, 0, len(array) - 1)
print array
print solu.binary_search(array, 1)

# print solu.mergeSort(array)

# pre = [1, 2, 4, 5, 3]
# tin = [4, 2, 5, 1, 3]
# print solu.reConstructBinaryTree(pre, tin).left.val
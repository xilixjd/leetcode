# -*- coding: utf-8 -*-
'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
'''


class ReSolution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums = nums[k + 1:] + nums[:k + 1]
        print nums


re = ReSolution()
re.rotate([1,2,3,4,5,6,7], 3)


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        return nums

    def rotate2(self, nums, k):
        '''
        Step 1 - 12345 6789 ---> 54321 6789

        Step 2 - 54321 6789 ---> 54321 9876

        Step 3 - 543219876 ---> 678912345
        '''
        n = len(nums)
        k = k % len(nums)
        self.reverse(0, n - k - 1, nums)
        print nums
        self.reverse(n - k, n - 1, nums)
        print nums
        self.reverse(0, n - 1, nums)
        return nums


    def reverse(self, start, end, nums):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

solu = Solution()
print solu.rotate2([1,2], 0)
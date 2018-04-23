# -*- coding: utf-8 -*-
'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''


class ReSolution(object):
    def findDuplicates(self, nums):
        """
        非 extra space
        :type nums: List[int]
        :rtype: List[int]
        """
        record_array = [[] for i in range(len(nums))]
        res = []
        for n in nums:
            if len(record_array[n - 1]) > 0:
                res.append(n)
            else:
                record_array[n - 1].append(n)
        return res

    def findDuplicates2(self, nums):
        '''
        https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/92390/Python-O(n)-time-O(1)-space
        将数组本身当作 HashTable
        :param nums:
        :return:
        '''
        res = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                res.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1
        return res

re = ReSolution()
print re.findDuplicates2([4,3,2,7,8,2,3,1])


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_dict = {}
        array = []
        for n in nums:
            if nums_dict.get(n):
                nums_dict[n] += 1
            else:
                nums_dict[n] = 1

        for k in nums_dict:
            if nums_dict[k] > 1:
                array.append(k)
        return array

solu = Solution()
print solu.findDuplicates([4,3,2,7,8,2,3,1])
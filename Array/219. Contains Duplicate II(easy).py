# -*- coding: utf-8 -*-
'''
Given an array of integers and an integer k,
 find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
 and the absolute difference between i and j is at most k.

'''


class ReSolution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def find_same(array, k):
            for i in range(1, len(array)):
                if array[i] - array[i - 1] <= k:
                    return True
            return False

        nums_dict = {}
        for i in range(len(nums)):
            if nums_dict.get(nums[i]) is not None:
                nums_dict[nums[i]].append(i)
                if find_same(nums_dict[nums[i]], k):
                    return True
            else:
                nums_dict[nums[i]] = [i]
        return False


re = ReSolution()
print re.containsNearbyDuplicate([1, 0, 1, 1], 4)


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_dict = {}
        for i, v in enumerate(nums):
            if v in nums_dict and i - nums_dict[v] <= k:
                return True
            else:
                nums_dict[v] = i
        return False


solu = Solution()
print solu.containsNearbyDuplicate([1,0,1,1], 1)
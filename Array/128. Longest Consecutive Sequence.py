# -*- coding: utf-8 -*-

'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        未通过 64 / 68 test cases passed.
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for n in nums:
            if nums_dict.get(n) is None:
                nums_dict[n] = set([n])
        for key in nums_dict:
            if key + 1 in nums_dict:
                nums_dict[key + 1] |= nums_dict[key]
                nums_dict[key] |= nums_dict[key + 1]
            if key - 1 in nums_dict:
                nums_dict[key - 1] |= nums_dict[key]
                nums_dict[key] |= nums_dict[key - 1]
        max_len = { 'length': 0}
        for key in nums_dict:
            if max_len['length'] < len(nums_dict[key]):
                max_len['length'] = len(nums_dict[key])
                max_len['key'] = key
        max_set = set()
        for k in nums_dict[max_len['key']]:
            max_set |= nums_dict[k]

        # print nums_dict
        print max_set
        return len(max_set)

    def longestConsecutiveFast(self, nums):
        nums_dict = {}
        res = 0
        for n in nums:
            if nums_dict.get(n) is None:
                left = nums_dict.get(n - 1, 0)
                right = nums_dict.get(n + 1, 0)
                sums = left + right + 1
                nums_dict[n] = sums
                res = max(res, sums)
                nums_dict[n - left] = sums
                nums_dict[n + right] = sums
        return res

    def longestConsecutive2(self, nums):
        '''
        Time limit exceeded
        :param nums:
        :return:
        '''
        res = 0
        for n in nums:
            if not n - 1 in nums:
                y = n + 1
                while y in nums:
                    y += 1
                res = max(res, y - n)
        return res


solu = Solution()
print solu.longestConsecutive2([-9,-4,9,-7,0,7,3,-1,6,2,-2,8,-2,0,2,-7,-5,-2,6,-5,0,-8,8,1,0,6,8,-8,-1])
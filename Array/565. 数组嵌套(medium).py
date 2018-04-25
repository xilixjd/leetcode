# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

Example 1:
Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
Note:
N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of A is an integer within the range [0, N-1].
'''


class Solution(object):
    def arrayNesting(self, nums):
        """
        超时 853/856
        :type nums: List[int]
        :rtype: int
        """
        # max_count = 0
        # for i in range(len(nums)):
        #     count = 1
        #     max_dict = {}
        #     max_dict[i] = 1
        #     the_num = nums[i]
        #     while the_num != i and max_dict.get(the_num) is None:
        #         max_dict[the_num] = 1
        #         count += 1
        #         the_num = nums[the_num]
        #     if max_count < count:
        #         max_count = count
        # return max_count

        max_count = 0
        # visited = [False for i in range(len(nums))]
        visited = {}
        for i in range(len(nums)):
            count = 1
            the_num = nums[i]
            while the_num != i and visited.get(the_num) is None:
                count += 1
                visited[the_num] = True
                the_num = nums[the_num]
            max_count = max(max_count, count)
        return max_count

    def arrayNesting2(self, nums):
        max_count = 0
        visited = [False for i in range(len(nums))]
        for i in range(len(nums)):
            count = 1
            the_num = nums[i]
            while the_num != i and not visited[the_num]:
                count += 1
                visited[the_num] = True
                the_num = nums[the_num]
            max_count = max(max_count, count)
        return max_count


solu = Solution()
print solu.arrayNesting2([5,4,0,3,1,6,2])
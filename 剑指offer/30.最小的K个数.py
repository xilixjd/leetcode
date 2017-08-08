# -*- coding:utf-8 -*-
'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''
import random
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k < 1 or k > len(tinput):
            return []
        index = self.partition(tinput, 0, len(tinput) - 1)
        while index != k - 1:
            print index
            if index > k - 1:
                index = self.partition(tinput, 0, index - 1)
            else:
                index = self.partition(tinput, index + 1, len(tinput) - 1)
        return tinput[:index + 1]


    def partition(self, numbers, start, end):
        index = random.randint(start, end)
        numbers[index], numbers[end] = numbers[end], numbers[index]
        small = start - 1
        for i in range(start, end):
            if numbers[i] < numbers[end]:
                small += 1
                if small != i:
                    numbers[small], numbers[i] = numbers[i], numbers[small]
        small += 1
        numbers[small], numbers[end] = numbers[end], numbers[small]
        return small

solu = Solution()
print solu.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 8)
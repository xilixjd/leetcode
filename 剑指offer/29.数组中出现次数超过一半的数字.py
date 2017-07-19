# -*- coding:utf-8 -*-
'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
import random

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        middle = len(numbers) / 2
        start = 0
        end = len(numbers) - 1
        index = self.partition(numbers, start, end)
        while index != middle:
            if index > middle:
                index = self.partition(numbers, start, index - 1)
            else:
                index = self.partition(numbers, index + 1, end)
        if self.check(numbers, numbers[middle]):
            return numbers[middle]
        else:
            return 0

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

    def check(self, numbers, number):
        times = 0
        for i in range(len(numbers)):
            if numbers[i] == number:
                times += 1
        if times * 2 <= len(numbers):
            return False
        return True

solu = Solution()
a = [4,5,3,1,4,6,9]
print solu.MoreThanHalfNum_Solution(a)
print a
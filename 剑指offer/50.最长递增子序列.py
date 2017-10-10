# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

def getDp1(array):
    dp = [0 for i in range(len(array))]
    for i in range(len(array)):
        dp[i] = 1
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def generateArray(array, dp):
    length = 0
    index = 0
    for i in range(len(dp)):
        if dp[i] > length:
            length = dp[i]
            index = i
    lis = [0 for i in range(length)]
    length -= 1
    lis[length] = array[index]
    for i in range(index + 1)[::-1]:
        if array[i] < array[index] and dp[i] == dp[index] - 1:
            length -= 1
            lis[length] = array[i]
            index = i
    return lis


# array = [1,2,5,6,3,7]
array = list("test")
dp = getDp1(array)
print generateArray(array, dp)
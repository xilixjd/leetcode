# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 
第 3 轮，每三个灯泡切换一次开关（如果关闭，则打开，如果打开则关闭）。对于第 i 轮，你每 i 个灯泡切换一次开关。 
对于第 n 轮，你只切换最后一个灯泡的开关。 找出 n 轮后有多少个亮着的灯泡。

示例:

给定 n = 3。状态off表示灯泡关闭，on表示开启。

初始时, 灯泡状态 [off, off, off].
第一轮后, 灯泡状态 [on, on, on].
第二轮后, 灯泡状态 [on, off, on].
第三轮后, 灯泡状态 [on, off, off]. 

你应该返回1，因为只有一个灯泡还亮着。
'''


class Solution(object):
    def bulbSwitch2(self, n):
        import math
        return int(math.sqrt(n))

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # array = [1 for i in range(n)]
        # i = 2
        # while i <= n:
        #     for j in range(i - 1, len(array), i):
        #         if array[j] == 1:
        #             array[j] = 0
        #         else:
        #             array[j] = 1
        #     i += 1
        # count = 0
        # for a in array:
        #     if a == 1:
        #         count += 1
        # return count

        count_dict = {}

        def count_div(num):
            temp = n = num
            count = 0
            while temp >= 2 and n >= 2:
                if temp % n == 0:
                    if count_dict.get(n) is not None:
                        count += count_dict[n]
                        temp /= n
                    else:
                        n -= 1
                        count += 1
                n -= 1
            count_dict[num] = count
            return count

        array = [0 for i in range(n)]
        for i in range(n):
            pos = i + 1
            temp_count = count_div(pos)
            if temp_count % 2 == 0:
                array[i] = 1
            else:
                array[i] = 0
        print array

solu = Solution()
print solu.bulbSwitch(100)

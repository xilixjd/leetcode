# -*- coding: utf-8 -*-
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution(object):
    def convertMy(self, s, numRows):
        """
        time limit ......
        :type s: str
        :type numRows: int
        :rtype: str
        """
        array = []
        arr = []
        re_minus = 0
        if numRows == 1:
            return s
        if numRows == 2:
            j = 1
            for i in range(len(s)):
                if (i + 1) % 2:
                    arr.append(s[i])
                    if j < len(s):
                        arr.append(s[j])
                    array.append(arr)
                    arr = []
                    j += 2

            if len(array[-1]) < numRows:
                x = numRows - len(array[-1])
                for y in range(x):
                    array[-1].append(0)
        else:
            for i in range(len(s)):
                re = (i + 1) % (numRows + numRows - 2)
                if re and re <= numRows:
                    arr.append(s[i])
                    re_minus = 0
                else:
                    re_minus += 1
                    # if re == 0:
                    #     re_minus = 2
                    array.append(arr)
                    arr_temp = [0 for j in range(numRows)]
                    arr_temp[numRows - re_minus - 1] = s[i]
                    array.append(arr_temp)
                    arr = []
            if re_minus == 0:
                x = numRows - len(arr)
                for y in range(x):
                    arr.append(0)
                array.append(arr)
        print array
        temp_str = ""
        for j in range(numRows):
            for i in range(len(array)):
                if len(array[i]) == numRows and array[i][j] != 0:
                    temp_str += array[i][j]
        print temp_str
        if temp_str == "":
            if len(array[0]) < numRows:
                return ''.join(array[0])
        return temp_str


    def convertFast(self, s, numRows):
        '''
        聪明方法
        :param s:
        :param numRows:
        :return:
        '''
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            print L
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)

    def convertFastMy(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        array = [''] * numRows
        index = 0
        step = 1
        for x in s:
            array[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(array)


solu = Solution()
print solu.convertFastMy('AB', 1)
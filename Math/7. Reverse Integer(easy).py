# -*- coding: utf-8 -*-

'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''


class ReSolution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        x_str = str(x)
        x_str_array = list(x_str)
        sign = x_str[0]
        positive_or_not = True
        if not sign.isdigit():
            positive_or_not = False
        if not positive_or_not:
            x_str_array = x_str_array[1:]
            x_str_array.reverse()
        else:
            x_str_array.reverse()
        i = 0
        while i < len(x_str_array):
            if x_str_array[i] == "0":
                x_str_array.pop(i)
            else:
                break
        res = int("".join(x_str_array))
        if res >= 2 ** 31:
            return 0
        return res if positive_or_not else -res

    def reverse2(self, x):
        """
        no extra space
        :type x: int
        :rtype: int
        """
        def get_div10_yushu(x):
            return x % 10

        if x == 0:
            return 0
        positive_or_not = True
        if x < 0:
            positive_or_not = False
        x = abs(x)
        temp_res = 0
        while x != 0:
            yushu = get_div10_yushu(x)
            temp_res = (temp_res * 10) + yushu
            x = x / 10
        if abs(temp_res) > 2 ** 31 - 1:
            return 0
        return temp_res if positive_or_not else -temp_res

re = ReSolution()
print re.reverse2(-12344)


class Solution(object):
    def reverseMy(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x is None:
            return None
        if x == 0:
            return 0
        x_str = str(x)
        if x_str.find('-') == -1:
            x_array = list(x_str)
            reversed_array = x_array
            reversed_array.reverse()
            i = 0
            while reversed_array[i] == '0':
                i += 1
            reversed_array = reversed_array[i:]
            reversed_str = ''.join(reversed_array)
            reversed_num = int(reversed_str)
        else:
            x_array = list(x_str[1:])
            reversed_array = x_array
            reversed_array.reverse()
            i = 0
            while reversed_array[i] == '0':
                i += 1
            reversed_array = reversed_array[i:]
            reversed_str = ''.join(reversed_array)
            reversed_num = int(reversed_str)
            reversed_num = -reversed_num
        if abs(reversed_num) > 2 ** 31 - 1:
            return 0
        return reversed_num

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        while x != 0:
            tail = self.negativeNumDivYushu(x, 10)
            new_result = result * 10 + tail
            if (new_result - tail) / 10 != result:
                return 0
            result = new_result
            x = self.negativeNumDivision(x, 10)
        if abs(result) > 2 ** 31 - 1:
            return 0
        return result

    def negativeNumDivision(self, num1, num2):
        if num1 < 0:
            num1 = -num1
            return - (num1 / num2)
        else:
            return num1 / num2

    def negativeNumDivYushu(self, num1, num2):
        if num1 < 0:
            num1 = -num1
            return - (num1 % num2)
        else:
            return num1 % num2

# solu = Solution()
# print solu.reverse(00000)
# -*- coding: utf-8 -*-
'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''


def reverse2(self, x):
    """
    no extra space
    :type x: int
    :rtype: int
    """


class ReSolution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def reverse_int(x):
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

        if x < 0:
            return False
        return reverse_int(x) == x


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = self.reverse(x)
        return y == x

    def reverse(self, x):
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


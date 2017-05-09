# -*- coding: utf-8 -*-

'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rom_array = [
            ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["", "M", "MM", "MMM"]
        ]
        rom_str = ""
        rom_str += rom_array[3][num / 1000 % 10]
        rom_str += rom_array[2][num / 100 % 10]
        rom_str += rom_array[1][num / 10 % 10]
        rom_str += rom_array[0][num % 10]
        return rom_str

solu = Solution()
print solu.intToRoman(4)
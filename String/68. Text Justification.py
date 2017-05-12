# -*- coding: utf-8 -*-
'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
'''


class Solution(object):
    def fullJustifyMy(self, words, maxWidth):
        """
        97% !!!!!!
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # if maxWidth == 0:
        #     return [""]
        temp_line_len = 0
        temp_line_index_array = []
        i = 0
        result = []
        while i < len(words):
            temp_line_len += len(words[i]) + 1
            if temp_line_len - 1 <= maxWidth:
                temp_line_index_array.append(i)
                i += 1
            else:
                temp_line_str = ""
                temp_line_array = []
                for j in range(len(temp_line_index_array)):
                    temp_line_str += words[temp_line_index_array[j]]
                    temp_line_array.append(words[temp_line_index_array[j]])

                result.append(self.insertBlank(temp_line_array, maxWidth, i == len(words)))
                temp_line_len = 0
                temp_line_index_array = []
            if i == len(words):
                temp_line_str = ""
                temp_line_array = []
                for j in range(len(temp_line_index_array)):
                    temp_line_str += words[temp_line_index_array[j]]
                    temp_line_array.append(words[temp_line_index_array[j]])
                result.append(self.insertBlank(temp_line_array, maxWidth, i == len(words)))
                break
        return result

    def insertBlank(self, array, maxWidth, flag):
        total_length = 0
        for a in array:
            total_length += len(a)
        print total_length
        if not flag:
            if len(array) == 1:
                return ''.join(array) + ' ' * (maxWidth - total_length)
            else:
                divide_num = (maxWidth - total_length) / (len(array) - 1)
                remainder = (maxWidth - total_length) % (len(array) - 1)
                string = ""
                for i in range(len(array) - 1):
                    if remainder != 0:
                        string += array[i] + ' ' * (divide_num + 1)
                        remainder -= 1
                    else:
                        string += array[i] + ' ' * divide_num
                if len(array) != 0:
                    string += array[len(array) - 1]
                return string
        else:
            if len(array) == 1:
                return ''.join(array) + ' ' * (maxWidth - total_length)
            else:
                string = ""
                for i in range(len(array)):
                    if i == len(array) - 1:
                        string += array[i]
                    else:
                        string += array[i] + " "
                string += ' ' * (maxWidth - len(string))
                return string





solu = Solution()
# print solu.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
# print solu.fullJustify(["What","must","be","shall","be."], 12)
# print solu.insertBlank(["world","owes","you","a","living;","the"], 30, False)
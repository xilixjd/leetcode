# -*- coding: utf-8 -*-
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, a
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class ReSolution(object):
    def isValidMy(self, s):
        stack = [1]
        for i in range(len(s)):
            if s[i] == ')':
                if stack[len(stack) - 1] != '(':
                    return False
                else:
                    stack.pop()
            elif s[i] == ']':
                if stack[len(stack) - 1] != '[':
                    return False
                else:
                    stack.pop()
            elif s[i] == '}':
                if stack[len(stack) - 1] != '{':
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])

        return len(stack) == 1

rs = ReSolution()
print rs.isValidMy(']')


class Solution(object):
    def isValid(self, s):
        '''
        用 stack 啊！！！
        :param s:
        :return:
        '''
        stack = [1]
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
            elif s[i] == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()
            elif s[i] == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
        return stack == [1]



    def isValidMy(self, s):
        """
        timelimit !!!!!!!!
        :type s_array: str
        :rtype: bool

        """
        brackets_dict = {
            'aa': '(',
            'ab': ')',
            'ca': '[',
            'cb': ']',
            'da': '{',
            'db': '}'
        }
        valid = True
        s_array = list(s)
        i = 0
        while len(s_array) > 0:
            if s_array[i] == ')' or s_array[i] == ']' or s_array[i] == '}':
                return False
            if s_array[i] == '(':
                aValid = False

                for j in range(i + 1, len(s_array), 2):
                    if s_array[j] == ')':
                        if self.judgeSingle(s_array[i+1:j]):
                            continue
                        aValid = True
                        s_array.pop(j)
                        s_array.pop(i)
                        break
                if not aValid:
                    return False
            elif s_array[i] == '[':
                bValid = False

                for j in range(i + 1, len(s_array), 2):
                    if s_array[j] == ']':
                        if self.judgeSingle(s_array[i+1:j]):
                            continue
                        bValid = True
                        s_array.pop(j)
                        s_array.pop(i)
                        break
                if not bValid:
                    return False
            elif s_array[i] == '{':
                cValid = False
                for j in range(i + 1, len(s_array), 2):
                    if s_array[j] == '}':
                        if self.judgeSingle(s_array[i+1:j]):
                            continue
                        cValid = True
                        s_array.pop(j)
                        s_array.pop(i)
                        break
                if not cValid:
                    return False
        return valid

    def judgeOdd(self, n):
        return n % 2 == 0

    def judgeSingle(self, array):
        a_dict = {
            'aa': 0,
            'ab': 0,
            'ca': 0,
            'cb': 0,
            'da': 0,
            'db': 0
        }
        for i in range(len(array)):
            if array[i] == '(':
                a_dict['aa'] += 1
            if array[i] == ')':
                a_dict['aa'] -= 1
            if array[i] == '[':
                a_dict['ca'] += 1
            if array[i] == ']':
                a_dict['ca'] -= 1
            if array[i] == '{':
                a_dict['da'] += 1
            if array[i] == '}':
                a_dict['da'] -= 1
        for k in a_dict:
            if a_dict[k] != 0:
                return True
        return False

solu = Solution()
print solu.isValid(']')
# ([()[]])
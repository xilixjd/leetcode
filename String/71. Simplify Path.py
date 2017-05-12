# -*- coding: utf-8 -*-
'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        skip = ['..', '.', '']
        print path.split('/')
        for dir in path.split('/'):
            if dir == '..' and len(stack) != 0:
                stack.pop()
            elif not dir in skip:
                stack.append(dir)
        res = ""
        for dir in stack:
            res += '/' + dir
        return '/' if len(res) == 0 else res

solu = Solution()
print solu.simplifyPath('/./home/dir')
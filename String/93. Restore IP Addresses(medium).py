# -*- coding: utf-8 -*-

'''
Given a string containing only digits,
restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''


class ReSolution(object):
    def restoreIpAddresses(self, s):
        def check(ip):
            if ip[0] == "0":
                return len(ip) == 1
            if int(ip) <= 255:
                return True
            else:
                return False

        if len(s) > 12:
            return []
        res = []
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                for k in range(j + 1, len(s) - 1):
                    ip1 = s[:i + 1]
                    ip2 = s[i + 1: j + 1]
                    ip3 = s[j + 1: k + 1]
                    ip4 = s[k + 1:]
                    if check(ip1) and check(ip2) and check(ip3) and check(ip4):
                        ip = ip1 + '.' + ip2 + '.' + ip3 + '.' + ip4
                        res.append(ip)
        return res

re = ReSolution()
print re.restoreIpAddresses('1111')

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        ret = []
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                for k in range(j + 1, len(s) - 1):
                    ip1 = s[:i+1]
                    ip2 = s[i+1: j+1]
                    ip3 = s[j+1: k+1]
                    ip4 = s[k+1:]
                    if self.check(ip1) and self.check(ip2) and self.check(ip3) and self.check(ip4):
                        ip = ip1 + '.' + ip2 + '.' + ip3 + '.' + ip4
                        ret.append(ip)
        return ret


    def check(self, s):
        num = int(s)
        if s[0] == '0':
            return len(s) == 1
        else:
            if num <= 255:
                return True
            else:
                return False

solu = Solution()
print solu.restoreIpAddresses('25525511135')
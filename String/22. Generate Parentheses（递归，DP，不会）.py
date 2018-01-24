# -*- coding: utf-8 -*-
'''
Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class ReSolution(object):
    def generateParenthesis1(self, n):
        '''
        二刷还是不会
        思路 1：暴力法 （击败 0.53%）
        将 n 对括号（2n 个括号）全排列的情况，则有 2 的 2n 次方种情况
        剔除掉不符合规则的括号情况
        用递归的方法去做，n 个 "(" 的组合即一个 "(" 加上 n - 1 个 "(" 的组合
        n 个 ")" 的组合即一个 ")" 加上 n - 1 个 ")" 的组合
        :param n:
        :return:
        '''
        res = []
        def generate(ans = []):
            if len(ans) == 2 * n:
                if validParenthesis(ans):
                    res.append("".join(ans))
            else:
                ans.append("(")
                generate(ans)
                ans.pop()
                ans.append(")")
                generate(ans)
                ans.pop()

        def validParenthesis(par):
            balance = 0
            for i in range(len(par)):
                if par[i] == "(":
                    balance += 1
                elif par[i] == ")":
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        generate()
        return res

    def generateParenthesis2(self, n):
        '''
        思路 2：回朔法 (击败 54%)
        规则：若 "(" 括号数小于 n，则添加 "("
        若 ")" 括号数小于 "("，则添加 ")"
        :param n:
        :return:
        '''
        res = []
        def backtrack(s = "", left = 0, right = 0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)
        backtrack()
        return res

    def generateParenthesis3(self, n):
        '''
        Let us consider an example to get clear view:

        f(0): ""

        f(1): "("f(0)")"

        f(2): "("f(0)")"f(1), "("f(1)")"

        f(3): "("f(0)")"f(2), "("f(1)")"f(1), "("f(2)")"

        So f(n) = "("f(0)")"f(n-1) , "("f(1)")"f(n-2) "("f(2)")"f(n-3) ... "("f(i)")"f(n-1-i) ... "(f(n-1)")"
        '''
        res = [['']]
        for i in range(1, n + 1):
            l = []
            for j in range(i):
                for first in res[j]:
                    for second in res[i - j - 1]:
                        l.append("(" + first + ")" + second)
            res.append(l)
        return res[n]


rs = ReSolution()
print rs.generateParenthesis3(3)


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        self.backtrack(list, "", 0, 0, n)
        return list

    def backtrack(self, list, s, open, close, m):
        if len(s) == m * 2:
            list.append(s)
            print "list", s
            return
        if open < m:
            print "open", open, s
            self.backtrack(list, s + '(', open + 1, close, m)
        if close < open:
            print "close", close, s
            self.backtrack(list, s + ')', open, close + 1, m)

    def generateParenthesisDp(self, n):
        '''
        public class Solution
{
    public List<String> generateParenthesis(int n)
    {
        List<List<String>> lists = new ArrayList<>();
        lists.add(Collections.singletonList(""));

        for (int i = 1; i <= n; ++i)
        {
            final List<String> list = new ArrayList<>();

            for (int j = 0; j < i; ++j)
            {
                for (final String first : lists.get(j))
                {
                    for (final String second : lists.get(i - 1 - j))
                    {
                        list.add("(" + first + ")" + second);
                    }
                }
            }

            lists.add(list);
        }

        return lists.get(lists.size() - 1);
    }
}
        Let us consider an example to get clear view:

        f(0): ""

        f(1): "("f(0)")"

        f(2): "("f(0)")"f(1), "("f(1)")"

        f(3): "("f(0)")"f(2), "("f(1)")"f(1), "("f(2)")"

        So f(n) = "("f(0)")"f(n-1) , "("f(1)")"f(n-2) "("f(2)")"f(n-3) ... "("f(i)")"f(n-1-i) ... "(f(n-1)")"
        :param n:
        :return:
        '''
        lists = [['']]
        for i in range(1, n + 1):
            list = []
            for j in range(i):
                for first in lists[j]:
                    # print first
                    for second in lists[i - j - 1]:
                        list.append("(" + first + ")" + second)
            lists.append(list)
            print lists
        return lists[n]


solu = Solution()
# print solu.generateParenthesisDp(3)
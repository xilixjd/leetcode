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
        lists = ['']
        for i in range(1, n + 1):
            list = []
            for j in range(i):
                for first in lists[j]:
                    for second in lists[i - j]:
                        list.append("(" + first + ")" + second)
            lists.append(list)
        return lists


solu = Solution()
print solu.generateParenthesisDp(3)
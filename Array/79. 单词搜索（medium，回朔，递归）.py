# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def back_track(i, j, board, word, index):
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
                return False
            if index == len(word):
                return True

            if word[index] != board[i][j]:
                return False
            board[i][j] = '*'
            exist = back_track(i + 1, j, board, word, index + 1) or \
                back_track(i - 1, j, board, word, index + 1) or \
                back_track(i, j + 1, board, word, index + 1) or \
                back_track(i, j - 1, board, word, index + 1)
            board[i][j] = word[index]
            return exist

        for i in range(len(board)):
            for j in range(len(board[i])):
                if back_track(i, j, board, word, 0):
                    print i, j
                    return True
        return False


solu = Solution()
# print solu.exist([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ], 'ESAE')
print solu.exist([['a', 'a']], 'aaa')
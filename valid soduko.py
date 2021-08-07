# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 18:00:39 2021

@author: saadu
"""

class Solution(object):
   def isValidSudoku(self, board):
       List = input("enter the number: ")
       """
      :type board: List[List[str]]
      :rtype: bool
      """
       for i in range(9):
          row = {}
          column = {}
          block = {}
          row_cube = 3 * (i//3)
          column_cube = 3 * (i%3)
          for j in range(9):
             if board[i][j]!='.' and board[i][j] in row:
                 return False
             row[board[i][j]] = 1
             if board[j][i]!='.' and board[j][i] in column:
                 return False
             column[board[j][i]] = 1
             rc= row_cube+j//3
             cc = column_cube + j%3
             if board[rc][cc] in block and board[rc][cc]!='.':
                 return False
             block[board[rc][cc]]=1
             return True
ob1 = Solution()
print(ob1.isValidSudoku([
   ["5","3",".",".","7",".",".",".","."],
   ["6",".",".","1","9","5",".",".","."],
   [".","9","8",".",".",".",".","6","."],
   ["8",".",".",".","6",".",".",".","3"],
   ["4",".",".","8",".","3",".",".","1"],
   ["7",".",".",".","2",".",".",".","6"],
   [".","6",".",".",".",".","2","8","."],
   [".",".",".","4","1","9",".",".","5"],
   [".",".",".",".","8",".",".","7","9"]]))

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 14:34:32 2022

@author: VAGUE
"""

import math
import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]  # using single list to represent 3x3 board
    
    def print_board(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # tells us which number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
# =============================================================================
#         moves = []
#         for (i, x) in enumerate(self.board):
#             if x == " ":
#                 moves.append(i)
# =============================================================================
        # using list comprehension
        # ['X', 'X', 'O'] -> [(0, 'X'), (1, 'X'), (2, 'O')]
        return [i for i, x in enumerate(self.board) if x == " "]
    

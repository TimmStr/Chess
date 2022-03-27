import numpy as np
from tkinter import *
from tkinter import ttk


# King, Queen, Rook (Turm), Bishop, Knight, Pawn
# WRook=1        BRook=11
# WKnight=2      BKnight=12
# WWBishop=3     BBBishop=13
# WQueen=4       BQueen=14
# WKing=5        BKing=15
# WPawn=6        BPawn=16

class Board:
    def __init__(self):
        self.board = np.array([[11, 12, 13, 14, 15, 13, 12, 11],
                               [16, 16, 16, 16, 16, 16, 16, 16],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [6, 6, 6, 6, 6, 6, 6, 6],
                               [1, 2, 3, 4, 5, 3, 2, 1]])
        print(self.board)
        self.start_game()

    def start_game(self):
        root=Tk()
        frm=ttk.Frame(root,padding=10)
        frm.grid()
        ttk.Label(frm, text='Chess').grid(column=0, row=0)
        ttk.Button(frm, text='Quit',command=root.destroy).grid(column=1, row=0)
        root.mainloop()


b = Board()

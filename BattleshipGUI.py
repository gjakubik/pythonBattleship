import tkinter as tk
from tkinter import *
from Player import Player
from enum import Enum
import time
from Battleship import Battleship

class colLabels(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7
    I = 8
    J = 9

class BattleshipGUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Battleship Simulator")
        self.root.maxsize(1040, 720)
        self.root.config(bg="#6E6C6F")

        self.leftedge    = .02
        self.rightedge   = .63
        self.topedge     = .07
        self.bottomedge  = .52
        self.boardwidth  = .35
        self.boardheight = .365

        self.canvas = tk.Canvas(self.root, height=720, width=1040, bg="#6E6C6F")
        self.canvas.pack()

        self.boardFrames = [tk.Frame(self.root, bg="#05cde3") for i in range(0, 4)]

        self.boardFrames[0].place(relwidth=self.boardwidth, relheight=self.boardheight, relx=self.leftedge, rely=self.topedge)
        self.boardFrames[1].place(relwidth=self.boardwidth, relheight=self.boardheight, relx=self.rightedge, rely=self.topedge)
        self.boardFrames[2].place(relwidth=self.boardwidth, relheight=self.boardheight, relx=self.leftedge, rely=self.bottomedge)
        self.boardFrames[3].place(relwidth=self.boardwidth, relheight=self.boardheight, relx=self.rightedge, rely=self.bottomedge)

        self.cellWidth = 3

        self.playButton = Button(self.root, text="Play", command=self.playBattleship).place(relwidth=0.1, relheight=0.08, relx=.45, rely=.485)

        for i in range(0, 4):
            self.setupEmptyBoards(i)

        self.root.mainloop()

    def playBattleship(self):
        game = Battleship()

        self.setupBoards(game.players)

        game.play(self.root, self.boardFrames)

    def setupEmptyBoards(self, i):
        for row in range(0, 10):
            tk.Label(self.boardFrames[i], text=str(row+1), width=self.cellWidth, bg='#05cde3').grid(row=row+1, column=0)
            tk.Label(self.boardFrames[i], text=colLabels(row).name, width=self.cellWidth, bg='#05cde3').grid(row=0, column=row+1)
            for col in range(0, 10):
                tk.Label(self.boardFrames[i], bg='#05cde3', width=self.cellWidth, borderwidth=2, relief='groove').grid(row=row+1, column=col+1, padx=0, pady=0)


    def setupBoards(self, players):
        for player in players:
            for row in range(0, 10):
                tk.Label(self.boardFrames[player.playerNum-1], text=str(row+1), width=self.cellWidth, bg='#05cde3').grid(row=row+1, column=0)
                tk.Label(self.boardFrames[player.playerNum-1], text=colLabels(row).name, width=self.cellWidth, bg='#05cde3').grid(row=0, column=row+1)
                for col in range(0, 10):
                    state = player.board.array[row][col]
                    tempColor = '#05cde3'
                    if state == 1:
                        tempColor = "white"
                    elif state == 2:
                        tempColor = "#a3a3a3"
                    elif state == 3:
                        tempColor = "#f20a0a"

                    tk.Label(self.boardFrames[player.playerNum-1], bg=tempColor, width=self.cellWidth, borderwidth=2, relief='groove').grid(row=row+1, column=col+1, padx=0, pady=0)

    
    
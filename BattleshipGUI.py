import tkinter as tk
from tkinter import *
from Player import Player
from enum import Enum
import time

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

        self.canvas = tk.Canvas(self.root, height=720, width=1040, bg="#6E6C6F")
        self.canvas.pack()

        self.boardFrames = [tk.Frame(self.root, bg="#05cde3") for i in range(0, 4)]

        self.boardFrames[0].place(relwidth=0.35, relheight=0.365, relx=0.1, rely=0.12)
        self.boardFrames[1].place(relwidth=0.35, relheight=0.365, relx=0.55, rely=0.12)
        self.boardFrames[2].place(relwidth=0.35, relheight=0.365, relx=0.1, rely=0.55)
        self.boardFrames[3].place(relwidth=0.35, relheight=0.365, relx=0.55, rely=0.55)
        self.cellWidth = 3

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

    
    def updatePlayerBoard(self, player):
        print('updating board')
        print('Printing new labels')
        for row in range(0, 10):
            for col in range(0, 10):
                state = player.board.array[row][col]
                tempColor = '#05cde3'
                if state == 1:
                    tempColor = "white"
                elif state == 2:
                    tempColor = "#a3a3a3"
                elif state == 3:
                    tempColor = "#f20a0a"

                newLabel = tk.Label(self.boardFrames[player.playerNum], bg=tempColor, width=self.cellWidth, borderwidth=2, relief='groove')
                newLabel.grid(row=row+1, column=col+1, padx=0, pady=0)

        self.root.update_idletasks()
        self.root.update()
        time.sleep(20)
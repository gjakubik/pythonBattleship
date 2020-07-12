#!/usr/bin/env python3

from Board import Board
from Player import Player
import tkinter as tk
from tkinter import *
import time

class Battleship():

    def __init__(self):
        self.players =[Player(i) for i in range(0, 4)]
        self.cellWidth = 3

        for player in self.players:
            player.setPlaceStrat('random')
            player.setShotStrat('random')
            player.placeShips()

    def play(self, root, boardFrames):
        # Set vars to keep track of game status and current player
        gameOn = True
        i = 0
        n = 0

        while gameOn:
            n += 1
            currentPlayer = self.players[i]
            nextPlayer = self.findNextPlayer(self.players, i)
            if i == 3:
                i = 0
            else:
                i += 1
        
            currentPlayer.shootShips(nextPlayer)
            self.updatePlayerBoard(root, boardFrames, nextPlayer)
            
            if n > 10:
                gameOn = False



    def findNextPlayer(self, players, i):
        while players[i+1 if i != 3 else 0].inGame == False:
            i += 1

        return players[i+1]

    def updatePlayerBoard(self, root, boardFrames, player):
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

                newLabel = tk.Label(boardFrames[player.playerNum], bg=tempColor, width=self.cellWidth, borderwidth=2, relief='groove')
                newLabel.grid(row=row+1, column=col+1, padx=0, pady=0)

        time.sleep(1)



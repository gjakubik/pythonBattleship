#!/usr/bin/env python3

from Board import Board
from Player import Player
from BattleshipGUI import BattleshipGUI

class Battleship():

    def __init__(self):
        self.players =[Player(i) for i in range(0, 4)]

        self.myGUI = BattleshipGUI()

        for player in self.players:
            player.setPlaceStrat('random')
            player.setShotStrat('random')
            player.placeShips()

            self.myGUI.setupBoards(players)
        # Set vars to keep track of game status and current player
        self.gameOn = True
        self.i = 0

    def play():
        while self.gameOn:
            currentPlayer = self.players[i]
            nextPlayer = self.findNextPlayer(players, i)
            if i == 3:
                i = 0
            else:
                i += 1
        
            currentPlayer.shootShips(nextPlayer)
            self.myGUI.updatePlayerBoard(nextPlayer)
            self.gameOn = False



    def findNextPlayer(players, i):
        while players[i+1].inGame == False:
            i += 1

        return players[i+1]



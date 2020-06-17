import random
import time
from Board import Board

class Player():

    def __init__(self, playerNum):
        self.playerNum = playerNum
        self.placeStrat = ''
        self.shotStrat = ''
        self.inGame = True
        self.board = Board()

    def setPlaceStrat(self, placeStrat):
        self.placeStrat = placeStrat

    def getPlaceStrat(self):
        return self.placeStrat

    def setShotStrat(self, shotStrat):
        self.shotStrat = shotStrat

    def getShotStrat(self):
        return self.shotStrat
    
    def placeShips(self):
        self.board.placeShips(self.placeStrat)

    def shootShips(self, nextPlayer):
        if self.shotStrat == 'random':
            random.seed(time.time())

            shotRow = random.randint(0, 9)
            shotCol = random.randint(0, 9)

        #once shotRow and shotCol are determined, print the shot result and change board
        print(nextPlayer.board.shot(shotRow, shotCol))


    def printBoard(self):
        self.board.printBoard()
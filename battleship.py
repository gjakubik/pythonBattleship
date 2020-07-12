#!/usr/bin/env python3

from Board import Board
from Player import Player
from BattleshipGUI import BattleshipGUI

def playBattleship():

    players =[Player(i) for i in range(0, 4)]

    myGUI = BattleshipGUI()

    for player in players:
        player.setPlaceStrat('random')
        player.setShotStrat('random')
        player.placeShips()

    myGUI.setupBoards(players)
    gameOn = True
    i = 0

    #myGUI.root.mainloop()
    while gameOn:
        currentPlayer = players[i]
        if i == 3:
            i = 0
        else:
            i += 1
        
        
        myGUI.updatePlayerBoard(players[i+1])

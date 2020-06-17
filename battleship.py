#!/usr/bin/env python3

from Board import Board
from Player import Player

p1 = Player(1)
p2 = Player(2)

p1.setPlaceStrat('random')
p2.setPlaceStrat('random')

p1.setShotStrat('random')
p2.setShotStrat('random')

p1.placeShips()
p2.placeShips()

p1.shootShips(p2)

print(p1.shotStrat)

p1.board.printShips()
p2.board.printShips()

p1.printBoard()
p2.printBoard()

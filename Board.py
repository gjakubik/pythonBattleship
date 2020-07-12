from enum import Enum
import random
import time


class Status(Enum):
    EMPTY   = 0
    MISS    = 1
    SHIP    = 2
    HITSHIP = 3

class Direction(Enum):
    UP    = 0
    RIGHT = 1
    DOWN  = 2
    LEFT  = 3

class Ship():
    def __init__(self, size, startRow, startCol, endRow, endCol):
        self.size = size
        self.startRow = startRow
        self.startCol = startCol
        self.endRow = endRow
        self.endCol = endCol
        self.sunk = False

    def printShip(self):
        print(f'This ship is {self.size} spaces long')
        print(f'Starting at {self.startRow}, {self.startCol}')
        print('')



class Board():
    def __init__(self):
        self.array = [
            [Status.EMPTY.value for i in range(10)] for x in range(10)]
        self.inGame = True
        self.winner = False
        self.ships = []

    def printBoard(self):
        for row in self.array:
            print(row)

        print('\n')

    def printShips(self):
        for ship in self.ships:
            ship.printShip()

    def shot(self, row, col):
        if self.array[row][col] == Status.EMPTY.value:
            self.array[row][col] = Status.MISS.value
            shotResult = 'It\'s a miss!'

        elif self.array[row][col] == Status.SHIP.value:
            self.array[row][col] = Status.HITSHIP.value
            shotResult = 'It\'s a hit!'

        else:
            shotResult = 'Already guessed this space!'

        return shotResult

    # Run placeShip for each ship size
    def placeShips(self, placementType):
        shipSizes = [5, 4, 3, 3, 2]
        if placementType.lower() == 'random':
            for size in shipSizes:
                self.placeShip(size, 0, 9, 0, 9)
                #print(f'Placed {size} ship')

    def placeShip(self, shipSize, minRow, maxRow, minCol, maxCol):
        placedShip = False

        while placedShip != True:
            # Generate random seed
            random.seed(time.time())

            # Random space selection
            randRow = random.randint(minRow, maxRow)
            randCol = random.randint(minCol, maxCol)
            
            # Choose random direction
            direction = random.randint(0, 3)

            # Check if ship can be placed
            canPlace = self.checkPlacement(shipSize, randRow, randCol, direction)

            # If ship can be placed, iterate and change spaces in direction chosen
            if canPlace:
                if direction == Direction.UP.value:
                    for i in range(shipSize):
                        self.array[randRow - i][randCol] = Status.SHIP.value
                    
                    self.ships.append(Ship(shipSize, randRow, randCol, randRow - shipSize + 1, randCol))

                elif direction == Direction.RIGHT.value:
                    for i in range(shipSize):
                        self.array[randRow][randCol + i] = Status.SHIP.value

                    self.ships.append(Ship(shipSize, randRow, randCol, randRow, randCol + shipSize - 1))

                elif direction == Direction.DOWN.value:
                    for i in range(shipSize):
                        self.array[randRow + i][randCol] = Status.SHIP.value

                    self.ships.append(Ship(shipSize, randRow, randCol, randRow + shipSize - 1, randCol))

                else:
                    for i in range(shipSize):
                        self.array[randRow][randCol - i] = Status.SHIP.value   

                    self.ships.append(Ship(shipSize, randRow, randCol, randRow, randCol - shipSize + 1))

                placedShip = True

    # Check spots before placeShip function can actually change board state
    def checkPlacement(self, shipSize, startRow, startCol, direction):
        canPlace = True

        if direction == Direction.UP.value:
            for i in range(shipSize):
                if startRow - i < 0: 
                    canPlace = False
                elif self.array[startRow - i][startCol] == Status.SHIP.value:
                    canPlace = False

        elif direction == Direction.RIGHT.value:
            for i in range(shipSize):
                if startCol + i > 9:
                    canPlace = False
                elif self.array[startRow][startCol + i] == Status.SHIP.value:
                    canPlace = False
                    
        elif direction == Direction.DOWN.value:
            for i in range(shipSize):
                if startRow + i > 9:
                    canPlace = False
                elif self.array[startRow + i][startCol] == Status.SHIP.value:
                    canPlace = False

        else:
            for i in range(shipSize):
                if startCol - i < 0:
                    canPlace = False
                elif self.array[startRow][startCol - i] == Status.SHIP.value:
                    canPlace = False
        
        return canPlace



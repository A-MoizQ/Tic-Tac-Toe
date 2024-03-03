
turns = [
    ["","",""],
    ["","",""],
    ["","",""]
]

def gameRun(x,y,player,blockSize):
    column = checkIfColumnExists(x,blockSize)
    row = checkIfRowExists(y,blockSize)

    ''' Since the grid 3x3, we use array indexing to check where in the 2d array
        the user clicked coordinates exist '''
    
    if((column >= 0 and column <= 2) and (row >= 0 and row <= 2)):
        exitsCheck = checkIfAlreadyExists(column, row)

        if(exitsCheck == True):
            turns[row][column] = player

            ''' If any of the following statements are true it returns the following 3 things:
                1. The row where the required move is to be made
                2. The column where the required move is to be made
                3. The shape of the the player that did the move 

                And it returns false when player plays move outside the grid or if 
                the place where user did the move already has a character placed there.
            '''
            
            if(columnCheck(player,column) == 3):
                return row, column,player 
            
            elif(rowCheck(player,row) == 3):
                return row,column,player
            
            elif(firstDiagonalCheck(player) == 3):
                return row,column,player
            
            elif(secondDiagonalCheck(player) == 3):
                return row,column,player
            
            else:
                return row,column,0
            
        else:
            return False
        
    else:
        return False        

''' Checks if column exits in the grid '''
def checkIfColumnExists(x,blockSize):
    columnCheck = -1*(blockSize + blockSize/2)
    column = 0
    while column < 3:
        if(x > columnCheck and x < columnCheck+blockSize):
            return column
        else:
            column += 1
            columnCheck += blockSize
    column = 4
    return column

''' Checks if row exists in the grid '''
def checkIfRowExists(y,blockSize):
    rowCheck = (blockSize+blockSize/2)
    row = 0
    while row < 3:
        if(y < rowCheck and y > (rowCheck - blockSize)):
            return row
        else:
            row += 1
            rowCheck -= blockSize
    row = 4
    return row

''' Checks if the clicked tile on the grid already has a shape in it or not '''
def checkIfAlreadyExists(column,row):
    if turns[row][column] == "x":
        return False
    elif turns[row][column] == "o":
        return False
    else:
        return True

''' Checks if 3 same shapes come in a column '''
def columnCheck(player,column):
    i = 0
    count = 0
    while i < 3:
        if(turns[i][column] == player):
            count += 1
        i += 1
    
    if(count == 3):
        return count
    else:
        return False

''' Checks if 3 same shapes come in a row '''
def rowCheck(player,row):
    i = 0
    count = 0
    while i < 3:
        if(turns[row][i] == player):
            count += 1
        i += 1
    if count == 3:
        return count
    else:
        return False

''' Checks if 3 same shapes come in the first diagonal '''
def firstDiagonalCheck(player):
    i = 0
    count = 0
    while i < 3:
        if(turns[i][i] == player):
            count += 1
        i += 1
    
    if(count == 3):
        return count
    else:
        return False
    
''' Checks if 3 same shapes come in the second diagonal '''
def secondDiagonalCheck(player):
    i = 2
    j = 0
    count = 0
    while i >= 0:
        if(turns[j][i] == player):
            count += 1
        i -= 1
        j += 1
    if(count == 3):
        return count
    else:
        return False

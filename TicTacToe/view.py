from turtle import *
from controller import storeCoords
from time import sleep

window = Screen()
screenWidth = 800
screenHeight = 800
window.setup(screenWidth,screenHeight)
window.title("TicTacToe")

blockSize = screenWidth * 0.25  #block  size will always be 25% of the screen width

player1 = textinput("player 1 input", "Enter name for player o")
player2 = textinput("player 2 input", "Enter name for player x")

player = ["o","x"]

''' Function draws 2 shapes (o and x) based on which player did the move '''
def drawShape(character,run):
    if(character == player[0]):
        x, y, radius = findCenter(run)
        y -= radius-10
        turtleObj = Turtle()
        turtleObj.hideturtle()
        turtleObj.width(3)
        turtleObj.speed(0)
        turtleObj.pu()
        turtleObj.goto(x,y)
        turtleObj.pd()
        turtleObj.circle(radius-10)
    else:
        x, y, radius = findCenter(run)
        turtleObj = Turtle()
        turtleObj.hideturtle()
        turtleObj.width(3)
        turtleObj.speed(0)
        turtleObj.pu()
        turtleObj.goto(x,y)
        turtleObj.pd()
        turtleObj.left(45)
        turtleObj.forward(blockSize/2)
        turtleObj.left(180)
        turtleObj.forward(blockSize)
        turtleObj.left(180)
        turtleObj.forward(blockSize/2)
        turtleObj.left(90)
        turtleObj.forward(blockSize/2)
        turtleObj.left(180)
        turtleObj.forward(blockSize)



''' Used to find the center of a given block in the 3x3 grid for shape printing'''
def findCenter(run):
    x = -1*(blockSize + blockSize/2)
    y = blockSize + blockSize/2
    radius = blockSize/2
    column = 0
    row = 0
    while column != run[1]:
        x += blockSize
        column += 1
    while row != run[0]:
        y -= blockSize
        row += 1
        
    x += blockSize/2
    y -= blockSize/2
    return x,y,radius


''' Used to create the 3x3 grid '''
def createGrid():
    turtleObj = Turtle()
    turtleObj.speed(0)
    turtleObj.hideturtle()
    turtleObj.pu()
    turtleObj.width(3)
    #upper horizontal line
    x = (-1*(blockSize + blockSize/2))
    y = blockSize/2
    turtleObj.goto(x,y)
    turtleObj.pd()
    x += blockSize*3
    turtleObj.goto(x,y)
    #lower horizontal line
    y = -1*(blockSize/2)
    turtleObj.pu()
    turtleObj.goto(x,y)
    turtleObj.pd()
    x -= blockSize*3
    turtleObj.goto(x,y)
    #reset for vertical lines
    x,y = 0,0
    #for left vertical line
    x = -1*(blockSize/2)
    y += (blockSize + blockSize/2)
    turtleObj.pu()
    turtleObj.goto(x,y)
    turtleObj.pd()
    y -= blockSize*3
    turtleObj.goto(x,y)
    turtleObj.pu()
    #for right vertical line
    x = blockSize/2
    turtleObj.goto(x,y)
    turtleObj.pd()
    y += blockSize*3
    turtleObj.goto(x,y)
    turtleObj.pu()
    x,y= 0,0
    turtleObj.goto(x,y)


createGrid()
    
playerTurn = True

''' A function of onscreenclick from turtle library which recursively executes when the file is running '''
def coordinates(x,y):
    global playerTurn
    if playerTurn:
        run = storeCoords(x,y,player[0],blockSize)
        if run == False:
            showHeading("Invalid Move")
        else:
            drawShape(player[0],run)
            playerTurn = False
            if run[2] == player[0]:
                showHeading(player1 + " has won")
        
    else:
        run = storeCoords(x,y,player[1],blockSize)
        if run == False:
            showHeading("Invalid Move")
        else:
            drawShape(player[1],run)
            playerTurn = True
            if run[2] == player[1]:
                showHeading(player2 + " has won")
        
''' Used to show if player made Invalid move or if a certain player won '''
def showHeading(player):
    turtleObj = Turtle()
    turtleObj.speed(0)
    turtleObj.hideturtle()
    turtleObj.pu()
    turtleObj.goto(screenHeight/2-blockSize*2,screenWidth/2- blockSize/2)
    turtleObj.write(f"{player}", align="center",font=("Arial",16,"normal"))
    sleep(2)
    turtleObj.clear()
    if player == player1 + " has won" or player == player2 + " has won":
        window.exitonclick()
    

''' Main loop running the turtle library '''
running = True
while running:
    window.listen()
    onscreenclick(coordinates,1)
    window.mainloop()
    



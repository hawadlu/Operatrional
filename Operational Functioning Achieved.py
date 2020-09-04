from tkinter import *
from tkinter import ttk
import tkinter


def HTP ():
    global canvas
    global tkinter
    #Deletes an updates the canvas
    canvas.delete("all")
    canvas.create_text(300,100, fill="black",font="Times 40 bold", text="Operational")
    canvas.create_text(300,150, fill="black",font="Times 20 underline bold", text="How To play")
    canvas.update()

    #Adds instructions
    canvas.create_text(300,250, fill="black",font="Times 12", text="To win land on the target square with the correct total at the right time....\n\nUse the Arrow keys to move your total. Each move forward will add one unless \nthe square has a mathematical operation on it but beware, each move backwards \nwill subtract from your total. ")

    #Return To Home Button
    B = Button(font="Times 20 bold", text = "Return To Home", command = GenerateHome, anchor = CENTER)
    B.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    B_window = canvas.create_window(100, 400, width = 400, anchor=W, window=B)
    
def Play ():
    global tkinter
    global canvas

    #Deletes an updates the canvas
    canvas.delete("all")
    canvas.create_text(300,100, fill="black",font="Times 40 bold", text="Operational")
    canvas.create_text(300,150, fill="black",font="Times 20 underline bold", text="Play")
    canvas.update()
    
    #How to play button
    B1 = Button(root, font="Times 20 bold", text = "3 X 3", command = ThreeByThree, anchor = CENTER)
    B1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    B1_window = canvas.create_window(100, 200, width = 400, anchor=W, window=B1)

    #Play button
    B2 = Button(root, font="Times 20 bold", text = "4 X 4", command = FourByFour, anchor = CENTER)
    B2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    B2_window = canvas.create_window(100, 300, width = 400, anchor=W, window=B2)

    #Return to home
    GenerateReturnToHome(100, 400)

#Generates Grids
def GenerateGrid():
    global listUsed
    global listUsedCoordinates
    if intGameMode == 1:
        #Setting up the variables needed for repopulating the canvas
        intTop = 250
        intNumberCount = 0
        intLeft = 165
        #Populates the grid and checks to see if there are any Null Values
        for i in range(3):
            if Grid1.list[intNumberCount] == None:
                #No element
                pass
            else:
                #Does no print value of 0
                if Grid1.list[intNumberCount] == 1:
                    pass
                else:
                    canvas.create_text(intLeft, intTop, fill="black", font="Tines 15 bold", text = Grid1.list[intNumberCount])
            intLeft += 130
            intNumberCount += 1
        intTop += 100
        intLeft = 165

        for i in range(3):
            if Grid1.list[intNumberCount] == None:
                #No element
                pass
            else:
                #Does no print value of 0
                if Grid1.list[intNumberCount] == 1:
                    pass
                else:
                    canvas.create_text(intLeft, intTop, fill="black", font="Tines 15 bold", text = Grid1.list[intNumberCount])
            intLeft += 130
            intNumberCount += 1
        intTop += 100
        intLeft = 165
        for i in range(3):
            if Grid4.list[intNumberCount] == None:
                #No element
                pass
            else:
                #Does no print value of 0
                if Grid1.list[intNumberCount] == 1:
                    pass
                else:
                    canvas.create_text(intLeft, intTop, fill="black", font="Tines 15 bold", text = Grid1.list[intNumberCount])
            intLeft += 130
            intNumberCount += 1
            
    #Generates the 4 X 4 grid                       
    elif intGameMode ==2:
        #Setting up the variables needed for repopulating the canvas
        intTop = 237.5
        intNumberCount = 0
        intLeft = 150
        #Populates the grid and checks to see if there are any Null Values
        for i in range(4):
            if Grid4.list[intNumberCount] == None:
                #No element
                pass
            else:
                #Does no print value of 0
                if Grid4.list[intNumberCount] == 1:
                    pass
                else:
                    canvas.create_text(intLeft, intTop, fill="black", font="Tines 15 bold", text = Grid4.list[intNumberCount])
            intLeft += 100
            intNumberCount += 1
        intTop += 75
        intLeft = 150

        for i in range(4):
            if Grid4.list[intNumberCount] == None:
                #No element
                pass
            else:
                #Does no print value of 0
                if Grid4.list[intNumberCount] == 1:
                    pass
                else:
                    canvas.create_text(intLeft, intTop, fill="black", font="Tines 15 bold", text = Grid4.list[intNumberCount])
            intLeft += 100
            intNumberCount += 1
        intTop += 75
        intLeft = 150
        for i in range(4):
            if Grid4.list[intNumberCount] == None:
                #No element
                pass
            else:
                #Does no print value of 0
                if Grid4.list[intNumberCount] == 1:
                    pass
                else:
                    canvas.create_text(intLeft, intTop, fill="black", font="Tines 15 bold", text = Grid4.list[intNumberCount])
            intLeft += 100
            intNumberCount += 1
        intTop += 75
        intLeft = 150

        for i in range(4):
            if Grid4.list[intNumberCount] == None:
                #No element
                pass
            else:
                #Does no print value of 0
                if Grid4.list[intNumberCount] == 1:
                    pass
                else:
                    canvas.create_text(intLeft, intTop, fill="black", font="Tines 15 bold", text = Grid4.list[intNumberCount])
            intLeft += 100
            intNumberCount += 1

#Generates return to home button
def GenerateReturnToHome(x, y):
    #Return to home
    RTH = Button(font="Times 20 bold", text = "Return To Home", command = GenerateHome, anchor = CENTER)
    RTH.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    RTH_window = canvas.create_window(x, y, width = 400, anchor=W, window=RTH)
    

#Generates the home screen
def GenerateHome():
    #Defining and Reseting all necessary globals
    global listUsedCoordinates
    global listUsed
    global tkinter
    global intTotal
    global canvas
    global intClicked
    global listTotal
    listTotal = []
    intClikcked = 0
    intTotal = 0

    #Setting up lists
    global listUsedCoordinates
    global listUsed
    listUsed = []
    listUsedCoordinates = []

    global xLeft
    global xRight
    global yUp
    global yDown
    xLeft = 0
    xRight = 0
    yUp = 0
    yDown = 0

    #Deletes an updates the canvas
    canvas.delete("all")
    canvas.create_text(300,100, fill="black",font="Times 40 bold", text="Operational")
    canvas.update()
    
    #How to play button
    B1 = Button(root, font="Times 20 bold", text = "How To Play", command = HTP, anchor = CENTER)
    B1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    B1_window = canvas.create_window(100, 200, width = 400, anchor=W, window=B1)

    #Play button
    #TODO change quit to play
    B2 = Button(root, font="Times 20 bold", text = "Play", command = Play, anchor = CENTER)
    B2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    B2_window = canvas.create_window(100, 300, width = 400, anchor=W, window=B2)

    #Quit button
    B3 = Button(root, font="Times 20 bold", text = "Quit", command = quit, anchor = CENTER)
    B3.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    B3_window = canvas.create_window(100, 400, width = 400, anchor=W, window=B3)

def ThreeByThree():
    global listUsed
    listUsed = [7]
    global tkinter
    global canvas
    global intGameMode
    intGameMode = 1

    #Deletes an updates the canvas
    canvas.delete("all")
    canvas.create_text(300,100, fill="black",font="Times 40 bold", text="Operational")
    canvas.create_text(300,150, fill="black",font="Times 20 underline bold", text="Play")
    canvas.update()

    #Creating the Grid
    intLeft = 100
    intRight = 230
    intTop = 200
    intBottom = 300
    #loop that creates the canvas
    for i in range(3):
        canvas.create_rectangle(intLeft, intTop, intRight, intBottom, fill="beige", outline="black" )
        canvas.create_rectangle(intLeft, intTop + 100, intRight, intBottom + 100, fill="beige", outline="black")
        canvas.create_rectangle(intLeft, intTop + 200, intRight, intBottom + 200, fill="beige", outline="black")
        intLeft += 130
        intRight += 130

    #Creates the starting rectangle
    canvas.create_rectangle(100, 500, 230, 400, fill="blue", outline="black")
    canvas.pack()

    #Return to home
    GenerateReturnToHome(100, 550)

    #Populates The Grid
    GenerateGrid()
    #Gets posistion of canvas click
    canvas.bind("<Button-1>", callback)
    canvas.pack()

def FourByFour():
    global tkinter
    global canvas
    global listUsed
    global intGameMode
    intGameMode = 2
    listUsed = [12]

    #Deletes an updates the canvas
    canvas.delete("all")
    canvas.create_text(300,50, fill="black",font="Times 40 bold", text="Operational")
    canvas.create_text(300,100, fill="black",font="Times 20 underline bold", text="Play")
    canvas.update()

    #Setting up the variables needed for creating the canvas
    intLeft = 100
    intRight = 200
    intTop = 200
    intBottom = 325
    #loop that creates the canvas
    for i in range(4):
        canvas.create_rectangle(intLeft, intTop, intRight, intBottom, fill="beige", outline="black" )
        canvas.create_rectangle(intLeft, intTop + 75, intRight, intBottom + 75, fill="beige", outline="black")
        canvas.create_rectangle(intLeft, intTop + 150, intRight, intBottom + 150, fill="beige", outline="black")
        canvas.create_rectangle(intLeft, intTop + 225, intRight, intBottom + 175, fill="beige", outline="black")
        intLeft += 100
        intRight += 100

    canvas.create_rectangle(100, 425, 200, 500, fill="blue", outline="black")
    canvas.pack()

    #Generates the grid
    GenerateGrid()

    #Return to home
    GenerateReturnToHome(100, 550)

    #Gets posistion of canvas click
    canvas.bind("<Button-1>", callback)
    canvas.pack()

#Generrates only tiles and does no calculations
def SimpleGenerate():
    xLeft = listUsedCoordinates[-1][0]
    yUp = listUsedCoordinates[-1][1]
    xRight = listUsedCoordinates[-1][2]
    yDown = listUsedCoordinates[-1][3]
    canvas.create_rectangle(xLeft, yUp, xRight, yDown, fill="blue", outline="black" )
    
#Generates Blue Tiles
def GenerateTile(xLeft, yUp, xRight, yDown, intClicked):
    global listUsed
    global listUsedCoordinates
    #Checks to see if user has already clicked that tile
    if len(listUsed) != 0 and listUsed[-1] == intClicked:
        xLeft = listUsedCoordinates[-1][0]
        yUp = listUsedCoordinates[-1][1]
        xRight = listUsedCoordinates[-1][2]
        yDown = listUsedCoordinates[-1][3]
        canvas.create_rectangle(xRight, yUp, xLeft, yDown, fill="beige", outline="black")
        listUsedCoordinates.pop()
        listUsed.pop()

    #If tile is unclicked the game adds to appropriate lists
    else:
        #fills the clicked part of the canvas.
        canvas.create_rectangle(xRight, yUp, xLeft, yDown, fill="blue", outline="black")
        canvas.create_text(xLeft + 50, yUp + 50, fill="black",font="Times 12", text=intTotal)
        
        #Adding to the lists
        listUsed.append(intClicked)
        listUsedCoordinates.append([xLeft, yUp, xRight, yDown])
    #Repopulates the canvas

    
def callback(event):
    global listUsed 
    global intTotal
    global intClicked
    print("clicked at", event.x, event.y)

    #Setting up the variables needed for repopulating the canvas
    intLeft = 165
    intTop = 250
    intNumberCount = 0
    intClicked = 0

    #This part is for the 3 X 3 grid
    if intGameMode == 1:
        #Controls which part of the grid is being used based on it's vertical posistion. This does not need to be reset within the for loop.
        yUp = 200
        yDown = 300
        for i in range(3):
            #controls the horizontal part of the grid being used. It is reset for each row on the gridbeing
            xLeft = 100
            xRight = 230
            #where has the user clicked
            for i in range(3):
                intClicked += 1
                if event.x >= xLeft and event.x <=xRight and event.y >=yUp and event.y <=yDown:
                    #Checks to see if user has won
                    if intTotal == Grid1.WinningTotal - 1 and intClicked == Grid1.WinningSquare:
                        print("You won!!")
                        break
                    
                    #Working out the users score
                    if intClicked == listUsed[-1]:
                        intTotal -= Grid1.list[intClicked - 1]
                        print("Total", intTotal)
                    else:
                        print(Grid1.list[intClicked - 1])
                        intTotal += Grid1.list[intClicked - 1]
                        print("Total", intTotal)

                    GenerateTile(xLeft, yUp, xRight, yDown, intClicked)
                    #Adding the total
                    GenerateGrid()
                    #Breaks the loop after the definition is triggered
                    break
                else:
                    xLeft += 130
                    xRight += 130
            yUp += 100
            yDown += 100
        
    #This part if for the 4 X 4 Grid
    else:
        yUp = 200
        yDown = 275
        for i in range(4):
            #controls the horizontal part of the grid being used. It is reset for each row on the gridbeing
            xLeft = 100
            xRight = 200
            #where has the user clicked
            for i in range(4):
                intClicked += 1
                if event.x >= xLeft and event.x <=xRight and event.y >=yUp and event.y <=yDown:
                    #Checks to see if user has won
                    if intTotal == Grid4.WinningTotal - 1 and intClicked == Grid4.WinningSquare:
                        print("You won!!")
                        break
                    
                    #Working out the users score
                    if intClicked == listUsed[-1]:
                        intTotal -= Grid4.list[intClicked - 1]
                        print("Total", intTotal)
                    else:
                        print(Grid4.list[intClicked - 1])
                        intTotal += Grid4.list[intClicked - 1]
                        print("Total", intTotal)

                    GenerateTile(xLeft, yUp, xRight, yDown, intClicked)
                    #Adding the total
                    GenerateGrid()
                    #Breaks the loop after the definition is triggered
                    break
                else:
                    xLeft += 100
                    xRight += 100
            yUp += 75
            yDown += 75


            
class Grids:
    def __init__(self, list, WinningTotal, WinningSquare):
        self.list = list
        self.WinningTotal = WinningTotal
        self.WinningSquare = WinningSquare

    def GetValues(self):
        print("List:", self.list, " \n Winning Total:", self.WinningTotal, " \n Winning Square:", self.WinningSquare)
#Sets the grid layouts up
Grid1 = Grids([3, -2, 5, 1 , 1, -2, 1, 1, 1], 5, 3)
Grid4 = Grids([-1, 1, 17, 1, 1, 1, 3, 8, 1, 1, 1, 1, 1, -3, 1, 1], 17, 3)


Grid1.GetValues()
Grid4.GetValues()

#This is what starts the program
root = tkinter.Tk()
root.title("Operational")

#Sets up the game modes
global intGameMode
canvas = Canvas(root, width=600, height=600, bg = 'beige')
canvas.create_text(300,100, fill="black",font="Times 40 bold", text="Operational")
canvas.pack()
GenerateHome()

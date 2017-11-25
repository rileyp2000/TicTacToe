#This will be a calc
import sys
import time
import os
import string
import random
from random import randint
import webbrowser

board = ["1","2","3","4","5","6","7","8","9"]
isPlaceable = [True,True,True,True,True,True,True,True,True]

def initBoardPrint():
    print( "     |     |     ")
    print( "  1  |  2  |  3  ")
    print( "     |     |     ")
    print( "-----|-----|-----")
    print( "     |     |     ")
    print( "  4  |  5  |  6  ")
    print( "     |     |     ")
    print( "-----|-----|-----")
    print( "     |     |     ")
    print( "  7  |  8  |  9  ")
    print( "     |     |     ")
    print("\n\nReady to Begin?")

    
def printBoard():
    print()
    print( "     |     |     ")
    print( "  " + board[0]+"  |  "+board[1]+"  |  "+board[2]+"  ")
    print( "     |     |     ")
    print( "-----|-----|-----")
    print( "     |     |     ")
    print( "  " + board[3]+"  |  "+board[4]+"  |  "+board[5]+"  ")
    print( "     |     |     ")
    print( "-----|-----|-----")
    print( "     |     |     ")
    print( "  " + board[6]+"  |  "+board[7]+"  |  "+board[8]+"  ")
    print( "     |     |     ")




def checkGameStop(num):
    if checkTie() == True:
        print("Sorry, you tied!")
        time.sleep(2)
        sys.exit()
    elif checkPlayerWin() == True and num == 1:
        print("Congradulations, You beat a bot playing random spots!" +
              " You should be very proud!")
        time.sleep(2)
        sys.exit()
    elif checkCompWin() == True and num == 1:
        print("WOW, you lost to a bot playing random spots. Be better dude...")
        time.sleep(2)
        sys.exit()
    elif checkPlayerWin() == True and num == 2:
        print("Congradulations, You beat player 2!" +
              " You should be very proud!")
        time.sleep(2)
        sys.exit()
    elif checkCompWin() == True and num == 2:
        print("WOW, you beat player 1! Congrats!")
        time.sleep(2)
        sys.exit()
        

def checkTie():
    for openSpace in isPlaceable:
        if openSpace == True:
            return False
    return True 



def checkPlayerWin():
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        return True
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        return True
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        return True

    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        return True
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        return True
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        return True

    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        return True
    elif board[6] == "X" and board[4] == "X" and board[2] == "X":
        return True

    return False


def checkCompWin():
    if (board[0] == "O" and board[1] == "O" and board[2]) == "O":
        return True
    elif (board[3] == "O" and board[4] == "O" and board[5]) == "O":
        return True
    elif (board[6] == "O" and board[7] == "O" and board[8]) == "O":
        return True

    elif (board[0] == "O" and board[3] == "O" and board[6]) == "O":
        return True
    elif (board[1] == "O" and board[4] == "O" and board[7]) == "O":
        return True
    elif (board[2] == "O" and board[5] == "O" and board[8]) == "O":
        return True

    elif (board[0] == "O" and board[4] == "O" and board[8]) == "O":
        return True
    elif (board[6] == "O" and board[4] == "O" and board[2]) == "O":
        return True
    else:
        return False




def computerTurn():


    compCheck = compCheckWin()
    
    if compCheck != -1 and isPlaceable[compCheck] != False:
        board[compCheck] = "O"
        isPlaceable[compCheck] = False
        
    compCheck = compCheckThreat()
    
    if compCheck != -1 and isPlaceable[compCheck] != False:
        board[compCheck] = "O"
        isPlaceable[compCheck] = False  
    else:    
        spaceToGo = randint(0,8)    
        while isPlaceable[spaceToGo] == False:
            spaceToGo = randint(0,8)
        board[spaceToGo] = "O"
        isPlaceable[spaceToGo] == False


def compCheckThreat():
    whichSol = 0
    #all possible win configs
    row0= [board[0],board[1],board[2]]
    row1= [board[3],board[4],board[5]]
    row2= [board[6],board[7],board[8]]
    col0= [board[0],board[3],board[6]]
    col1= [board[1],board[4],board[7]]
    col2= [board[2],board[5],board[8]]
    diag0= [board[0],board[4],board[8]]
    diag1= [board[6],board[4],board[2]]

    allPos = [row0, row1, row2, col0, col1, col2, diag0, diag1]
    indInSol = 0
    isThreat = False
    
    for possible in allPos:
        if checkThreat(possible) != -1:
            indInSol = int(checkThreat(possible))
            isThreat = True
            break
        whichSol = whichSol + 1

    if isThreat == True:
        if whichSol == 0:
            return indInSol
        elif whichSol == 1:
            return indInSol + 3
        elif whichSol == 2:
            return indInSol + 6
        elif whichSol == 3:
            return indInSol * 3
        elif whichSol == 4:
            return (indInSol * 3) + 1
        elif whichSol == 5:
            return (indInSol *3) + 2
        elif whichSol == 6:
            return indInSol * 4
        elif whichSol == 7:
            return 6 - (indInSol * 2)
    else:
        return -1

def checkThreat(posWin):
    count = 0
    cO = 0
    index = 0
    for x in posWin:
        if x == "X":
            count = count + 1
        elif x == "O":
            cO = cO + 1
    if count == 2 and cO == 0:
        for x in posWin:
            if x != "X":
                return index
            index = index + 1
    else:
        return -1

def compCheckWin():
    whichSol = 0
    #all possible win configs
    row0= [board[0],board[1],board[2]]
    row1= [board[3],board[4],board[5]]
    row2= [board[6],board[7],board[8]]
    col0= [board[0],board[3],board[6]]
    col1= [board[1],board[4],board[7]]
    col2= [board[2],board[5],board[8]]
    diag0= [board[0],board[4],board[8]]
    diag1= [board[6],board[4],board[2]]

    allPos = [row0, row1, row2, col0, col1, col2, diag0, diag1]
    indInSol = 0
    isThreat = False
    
    for possible in allPos:
        if checkToWin(possible) != -1:
            indInSol = int(checkToWin(possible))
            isThreat = True
            break
        whichSol = whichSol + 1

    if isThreat == True:
        if whichSol == 0:
            return indInSol
        elif whichSol == 1:
            return indInSol + 3
        elif whichSol == 2:
            return indInSol + 6
        elif whichSol == 3:
            return indInSol * 3
        elif whichSol == 4:
            return (indInSol * 3) + 1
        elif whichSol == 5:
            return (indInSol *3) + 2
        elif whichSol == 6:
            return indInSol * 4
        elif whichSol == 7:
            return 6 - (indInSol * 2)
    else:
        return -1

def checkToWin(posWin):
    count = 0
    cO = 0
    index = 0
    for x in posWin:
        if x == "O":
            count = count + 1
        elif x == "X":
            cO = cO + 1
    if count == 2 and cO == 0:
        for x in posWin:
            if x != "O":
                return index
            index = index + 1
    else:
        return -1





    
def playSelf():
    while checkTie() == False:
        space = randint(0,8)
        while isPlaceable[space] == False:
            space = randint(0,8)
        board[space] = "X"
        isPlaceable[space] == False

        spaceToGo = randint(0,8)
        while isPlaceable[spaceToGo] == False:
            spaceToGo = randint(0,8)
        board[spaceToGo] = "O"
        isPlaceable[spaceToGo] == False

              
def playSinglePlayer(num):
    while True:
        #os.system('clear')
        printBoard()
    
        checkGameStop(num)
        
        choice = input("Please choose an empty space to put your X: ")
        if choice != "":
            choice = int(choice)-1
            if isPlaceable[choice] == True:
                board[choice] = "X"
                isPlaceable[choice] = False
                computerTurn()
            else:
                print("Invalid Placement, please choose again!")
                time.sleep(1)
        else:
            print("You need to put in a spot dummy")
            time.sleep(2)


def playMultiPlayer(num):
    while True:
        #os.system('clear')
        printBoard()
    
        checkGameStop(num)
        
        choice = input("Please choose an empty space to put your X: ")
        if choice != "":
            choice = int(choice)-1
            if isPlaceable[choice] == True:
                board[choice] = "X"
                isPlaceable[choice] = False
            else:
                print("Invalid Placement, please choose again!")
                time.sleep(1)
        else:
            print("You need to put in a spot dummy")
            time.sleep(2)

        checkGameStop(num)
        printBoard()

        choice = input("Please choose an empty space to put your O: ")
        if choice != "":
            choice = int(choice)-1
            if isPlaceable[choice] == True:
                board[choice] = "O"
                isPlaceable[choice] = False
            else:
                print("Invalid Placement, please choose again!")
                time.sleep(1)
        else:
            print("You need to put in a spot dummy")
            time.sleep(2)

        
def chooseGame(num):
    if num == 1:
        playSinglePlayer(num)
    elif num == 2:
        playMultiPlayer(num)
    elif num == 0:
        #playSelf()
        print("WOPR 3.1.5")
        print("I've learned since last time... this isnt a War Game anymore\nBeginning Thermonuclear Warfare Protocol 32B\n".upper())
        time.sleep(1)
        for x in range(0,8):
            print()
            print(''.join(random.choices(string.ascii_uppercase + string.digits, k=10)))
            time.sleep(.90)
        n1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        print("\n" + n1)
        time.sleep(.90)
        for y in range(0,2):
            print(n1)
            time.sleep(.90)
        print("\nCORRECT LAUNCH CODE FOUND\nBEGINNING LAUNCH SEQUENCE")
        time.sleep(1.5)
        print("3")
        time.sleep(1.5)
        print("2")
        time.sleep(1.5)
        print("1")
        time.sleep(1.5)
        webbrowser.open_new("http://bestanimations.com/Military/Explosions/nuclear-atom-bomg-explosion-animated-gif-5.gif")
        sys.exit()
    else:
        print("Invalid number of players")
        sys.exit()     


print("Welcome to Tic-Tac-Toe! \nA Game by Patrick Riley\nNovember 2017\n")
initBoardPrint()
numPlay = int(input("Enter the Number of players: "))
chooseGame(numPlay)






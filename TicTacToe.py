#This will be a calc
import sys
import time
from random import randint

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
    print("\n\n\nReady to Begin?")

    
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



def computerTurn():
    spaceToGo = randint(0,8)
    while isPlaceable[spaceToGo] == False:
        spaceToGo = randint(0,8)
    board[spaceToGo] = "O"
    isPlaceable[spaceToGo] == False



def checkTie():
    for openSpace in isPlaceable:
        if openSpace == True:
            return False
    return True 



def checkPlayerWin():
    if board[0] and board[1] and board[2] == "X":
        return True
    if board[3] and board[4] and board[5] == "X":
        return True
    if board[6] and board[7] and board[8] == "X":
        return True

    if board[0] and board[3] and board[6] == "X":
        return True
    if board[1] and board[4] and board[7] == "X":
        return True
    if board[2] and board[5] and board[8] == "X":
        return True

    if board[0] and board[4] and board[8] == "X":
        return True
    if board[6] and board[4] and board[2] == "X":
        return True

    return False


def checkCompWin():
    if (board[0] and board[1] and board[2]) == "O":
        return True
    if (board[3] and board[4] and board[5]) == "O":
        return True
    if (board[6] and board[7] and board[8]) == "O":
        return True

    if (board[0] and board[3] and board[6]) == "O":
        return True
    if (board[1] and board[4] and board[7]) == "O":
        return True
    if (board[2] and board[5] and board[8]) == "O":
        return True

    if (board[0] and board[4] and board[8]) == "O":
        return True
    if (board[6] and board[4] and board[2]) == "O":
        return True

    return False

    



print("Welcome to Tic-Tac-Toe! \nA Game by Patrick Riley\nNovember 2017\nn")
initBoardPrint()


while True:
    printBoard()
    
    if checkTie() == True:
        print("Sorry, you tied!")
        sys.exit()
    if checkPlayerWin() == True:
        print("Congradulations, You beat a bot playing random spots!" +
              " You should be very proud!")
        sys.exit()
    if checkCompWin() == True:
        print("WOW, you lost to a bot playing random spots. Be better dude...")
        sys.exit()
        
    choice = input("Please choose an empty space to put your X: ")

    if choice != "":
        choice = int(choice)-1
    else:
        print("You need to put in a spot dummy")
        sys.exit()
        
    if isPlaceable[choice] == True:
        board[choice] = "X"
        isPlaceable[choice] = False
        computerTurn()
    else:
        print("Invalid Placement, please choose again!")
        time.sleep(1)

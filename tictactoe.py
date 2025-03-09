import random


board = ['-' for x in range(9)]
currentPlayer = "X"
winner = None
gameIsRunning = True


# print the game board
def printBoard():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-"*10)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-"*10)
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
def playerInput():
    try:
        position = int(input("Enter a number from 1-9 to place the marker: "))
        if position >= 1 and position <= 9 and board[position-1] == "-":
            board[position-1] = currentPlayer
        else:
            print("Error. Please enter a different position")
            playerInput()
    except ValueError:
        print("Invalid input. Please enter a number from 1-9.")
        playerInput()


# check for win or tie
def checkHorizontal():
    global winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return True
    else:
        return False


def checkVertical():
    global winner
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]
        return True 
    else: 
        return False


def checkDiagonal():
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] != "-":
        winner = board[2]
        return True
    else: 
        return False
    

def checkTie():
    global gameIsRunning
    global board
    if "-" not in board:
        printBoard()
        print("It's a tie!")
        gameIsRunning = False
        if input("Would you like to play again? Type Y to continue.") == "Y":
            board = ['-' for x in range(9)]
            gameIsRunning = True


def checkWin():
    global gameIsRunning
    global board
    if checkHorizontal() or checkVertical() or checkDiagonal():
        printBoard()
        print(winner + " won!")
        gameIsRunning = False
        if input("Would you like to play again? Type Y to continue.") == "Y":
            board = ['-' for x in range(9)]
            gameIsRunning = True

# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# computer player
def computer():
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


# repeat until win or tie


while gameIsRunning:
    printBoard()
    playerInput()
    checkWin()
    checkTie()
    switchPlayer()
    computer()
    checkWin()
    checkTie()  





board = []

def init():
#initialize game board
        for i in range(0, 3): 
                board.append([])
                for j in range(0,3):
                        board[i].append('.')

def printBoard():
#print out board
        for i in range(0, 3): 
                for j in range(0,3):
                        print board[i][j],
                print

def play():
#play game

def check(let):
#check if a given player has won the game
#let represents X or O
#return True if game is won, False otherwise

def fullBoard():
#check if the board is full and there is no winner
#return True if the board is full, False otherwise

play()
#call function for game play

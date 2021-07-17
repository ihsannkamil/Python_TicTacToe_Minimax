# WELCOME TO MY GAME "TIC TAC TOE"
# LET'S SEE WHO'S WIN BRO...


# Initialized the board
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def boardprint(board):
    print(board[1] + '|' + board[2] + '|' + board[3] + '|')
    print('-•-•-•-')
    print(board[4] + '|' + board[5] + '|' + board[6] + '|')
    print('-•-•-•-')
    print(board[7] + '|' + board[8] + '|' + board[9] + '|')


# boardprint(board) – CHECK THE PROGRAM


# Initialized function to know whether or not space is free
def spaceisfree(position):
    if board[position] == ' ':
        return True
    else:
        return False


# print(spaceisfree(1)) – CHECK THE PROGRAM


# Initialized program for inserting letter
def checkdraw():
    for key in board.keys():
        if board[key] == ' ':
            return False  # Cause we still can play the game, if there's empty space
    return True  # There are no empty space left


def checkwin():
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] != ' ':
        return True
    else:
        return False


def whollwin(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == mark:
        return True
    else:
        return False


def insertletter(letter, position):
    if spaceisfree(position):
        board[position] = letter
        boardprint(board)
        if checkdraw():
            print('Huft, I almost got you bro! Yet, you survived with a draw!')
            exit()
        if checkwin():
            if letter == 'X':
                print("Again and again, I'm unstoppable")
                exit()
            else:
                print('There are no people who able to won against me, but you did it, congrats bro!')
                exit()
        return
    else:
        print('We already filled that space bro, cmon...')
        position = int(input('Choose another position: '))
        insertletter(letter, position)
        return


# define player move and AI move
player = '0'
AI = 'X'


def playermove():
    position = int(input("Enter the position for '0': "))
    insertletter(player, position)
    return


# BEFORE USING MINIMAX
"""
def aimove():
    position = int(input("Enter the position for 'X': "))
    insertletter(AI, position)
    return
"""


# AFTER USING MINIMAX
def aimove():
    bestscore = -1000
    bestmove = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = AI
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > bestscore:
                bestscore = score
                bestmove = key

    insertletter(AI, bestmove)
    return


def minimax(board, depth, ismaximizing):
    if whollwin(AI):
        return 100

    elif whollwin(player):
        return -100

    elif checkdraw():
        return 0

    if ismaximizing:
        bestscore = -1000

        for key in board.keys():
            if board[key] == ' ':
                board[key] = AI
                score = minimax(board, 0, False)
                board[key] = ' '
                if score > bestscore:
                    bestscore = score

        return bestscore

    else:
        bestscore = 1000

        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, 0, True)
                board[key] = ' '
                if score < bestscore:
                    bestscore = score

        return bestscore


while not checkwin():
    playermove()
    aimove()

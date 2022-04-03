
board = [" " for i in range(10)]
# board = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9]

def insertLetter(letter, pos):
    board[pos] = letter

def isspacefree(pos):
    return board[pos] == " "

def printBoard(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ")
    print("-------------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ")
    print("-------------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")


# If we have winner based on current board
def isWin(board, letter):
            # Horizontal, Vertical, Diagonal
    return(
            board[7] == letter and board[8] == letter and board[9] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[1] == letter and board[2] == letter and board[3] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter
        )


def playerMove():
    run = True
    while run:
        move = input("\nSelect Position (1-9) to place \'X\'  : ")

        try:
            move = int(move)
            if move > 0 and move < 10:
                if isspacefree(move):
                    run = False
                    insertLetter("X", move)

                else:
                    print("ERROR : Occupied Space")
            else:
                print("ERROR : Insert Number between 1 to 9")

        except:
            print("ERROR : Type Integer only")

def compMove():
    possibleMoves = [index for index, value in enumerate(board) if value == " " and index != 0]
    # Default move, Tie game
    move = 0

    # Check who win (checks for O first, X second)
    for letter in ["O", "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            # Placing letter in index of possible moves
            boardCopy[i] = letter

            # Check if winning
            if isWin(boardCopy, letter):
                move= i
                return move

    # Check if moving to corner is possible
    cornerOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornerOpen.append(i)


    # If can't move to corner
    if len(cornerOpen) > 0:
        move = selectRandom(cornerOpen)
        return move

    # Check if moving to center is possible
    if 5 in possibleMoves:
        move = 5
        return move

    # Check if moving to edge is possible
    edgeOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgeOpen.append(i)

    # If can't move to edge
    if len(edgeOpen) > 0:
        move = selectRandom(edgeOpen)

    return move


def selectRandom(lst):
    import random
    length = len(lst)
    r= random.randrange(0, length)
    return lst[r]


# We have in board variable one blank space (THATS WHY range(10))
# If we have more thn that one blank space, board not full
def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True



# Computer --> O
# Human --> X
def main():
    print("\nTIC TAC TOE")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWin(board, "O")):
            playerMove()
            printBoard(board)
        else:
            print("O Win [Computer]")
            break

        if not(isWin(board, "O")):
            move = compMove()
            # If computer cannot move
            if move == 0:
                # print("Tie")
                break
            else:
                insertLetter("O", move)
                print("\nComputer Placed an \'O\' in position ", move, ":")
                printBoard(board)
        else:
            print("X Win [Player]")
            break

    if isBoardFull(board):
        print("Tie")

if __name__ == "__main__":
    main()

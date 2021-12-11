def printBoard(board):
    for row in board:
        print(row)
    print()

def check(board, row, col):
    for i in range(col): 
        if (board[row][i]): 
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if(board[i][j]):
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while j >= 0 and i < 4:
        if(board[i][j]):
            return False
        i = i + 1
        j = j - 1
 
    return True

def solveProblem(board, col):
    if (col == n): 
        printBoard(board) 
        return True
    response = False
    for i in range(n):
        if(check(board, i, col)):
            board[i][col] = 1
            response = solveProblem(board, col+1) or response
            board[i][col] = 0

    return response
n = int(input("Size of the board: "))
board = [[0 for i in range(n)]for j in range(n)]
solveProblem(board, 0)

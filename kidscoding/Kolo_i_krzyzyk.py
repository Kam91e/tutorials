board = ['_'] * 9
def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

print_board()

while True:
    x = input('Pick a number form 0-8:')
    x = int(x)
    board[x] = 'X'
    print_board()
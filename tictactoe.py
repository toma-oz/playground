board = [
[' ', ' ', ' '],
[' ', ' ', ' '],
[' ', ' ', ' ']
]
    
def main():

    while True:

        print_board()
        print()
        playerX = input('X turn: ')
        x, y = playerX.split(' ')

        if board[int(x)-1][int(y)-1] != ' ':
            print('Try again')
            continue
        else:
            board[int(x)-1][int(y)-1] = 'X'
            winner = check_winner()
            if winner:
                print_board()
                print()
                print(f'{winner} wins!')
                break
        
        print_board()
        print()
        playerY = input('Y turn: ')
        x, y = playerY.split(' ')
        if board[int(x)-1][int(y)-1] != ' ':
            print('Try again')
            continue
        else:
            board[int(x)-1][int(y)-1] = 'Y'
            winner = check_winner()
            if winner:
                print_board()
                print()
                print(f'{winner} wins!')
                break




def check_input():
    ...
def check_winner():
    
    # Check rows
    if board[0][0] != ' ' and board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] != ' ' and board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] != ' ' and board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    
    # Check columns
    elif board [0][0] != ' ' and board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    elif board [0][1] != ' ' and board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    elif board [0][2] != ' ' and board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]

    # Check diagonals
    elif board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[2][0] != ' ' and board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]
    
def print_board():

    print('  1 2 3')
    print(f'1 {board[0][0]}|{board[0][1]}|{board[0][2]}')
    print('  -+-+-')
    print(f'2 {board[1][0]}|{board[1][1]}|{board[1][2]}')
    print('  -+-+-')
    print(f'3 {board[2][0]}|{board[2][1]}|{board[2][2]}')

main()
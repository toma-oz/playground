board = [
[' ', ' ', ' '],
[' ', ' ', ' '],
[' ', ' ', ' ']
]


def main():

    while True:

        playerx = player_x()
        if playerx:
            print(playerx)
            break
        playery = player_y()
        if playery:
            print(playery)
            break


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
    
    # Check for tie
    elif ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
        return 'tie'


def print_board():

    # Prints current game board
    print('  1 2 3')
    print(f'1 {board[0][0]}|{board[0][1]}|{board[0][2]}')
    print('  -+-+-')
    print(f'2 {board[1][0]}|{board[1][1]}|{board[1][2]}')
    print('  -+-+-')
    print(f'3 {board[2][0]}|{board[2][1]}|{board[2][2]}')


def player_x():

    while True:
        # Get player X input
        print_board()
        print()
        playerX = input('X turn: ')
        x, y = playerX.split(' ')

        # Check if input is valid
        if board[int(x)-1][int(y)-1] != ' ':
            print()
            print('Try again')
            print()
            continue

        # Store input in database, check for winner
        else:
            board[int(x)-1][int(y)-1] = 'X'
            winner = check_winner()
            if winner:
                print_board()
                print()
                if winner == 'tie':
                    return "It's a tie!!!"
                else:
                    return f'{winner} wins!'
            else:
                return False

def player_y():

    while True:

        # Get player Y input
        print_board()
        print()
        playerY = input('Y turn: ')
        x, y = playerY.split(' ')

        # Check if input is valid
        if board[int(x)-1][int(y)-1] != ' ':
            print()
            print('Try again')
            print()
            continue

        # Store input in database, check for winner
        else:
            board[int(x)-1][int(y)-1] = 'Y'
            winner = check_winner()
            if winner:
                print_board()
                print()
                if winner == 'tie':
                    return "It's a tie!!!"
                else:
                    return f'{winner} wins!'
            else:
                return False


if __name__ == '__main__':
    main()

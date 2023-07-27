test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1 = ''
player2 = ''
kor = 0

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker = ''
    global player1
    global player2
    global kor
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
        kor = kor + 1
    else:
        player2 = 'X'
        kor = kor + 1
    print(f'Player 1 go first')
    return player1,player2,kor

def position_choice(board):
    choice = 'wrong'
    global kor
    while choice not in ['1','2','3','4','5','6','7','8','9']:
        choice = input("Pick a position (1-9): ")
        if choice not in ['1','2','3','4','5','6','7','8','9']:
            print('Sorry, invalid choice! ')
    if kor % 2 == 0:
        board[int(choice)] = player2
        kor = kor + 1
    else:
        board[int(choice)] = player1
        kor = kor + 1

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

def play_again():
    global test_board
    global player1
    global player2
    global kor
    pa = input('Do you want to play again? Yes or No: ')
    if pa == 'Yes':
        test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        player1 = ''
        player2 = ''
        kor = 0
        game()
        return kor,test_board,player1,player2
    if pa == 'No':
        exit()
    else:
        exit()

def game():
    player_input()
    while win_check(test_board, 'X') == False and win_check(test_board, 'O') == False:
        display_board(test_board)
        position_choice(test_board)
    if win_check(test_board, 'X') == True or win_check(test_board, 'O') == True:
        display_board(test_board)
        if win_check(test_board, 'X') == True:
            print('X win!')
            play_again()
        if win_check(test_board, 'O') == True:
            print('O win!')
            play_again()
        else:
            pass

game()

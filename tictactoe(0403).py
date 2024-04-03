def print_board(board):
    for r in range(3):
        print(" " + board[r][0] + " | " + board[r][1] + " | " + board[r][2])
        if r != 2:
            print("---|---|---")

def check_win(board, player):
    # 가로, 세로, 대각선 검사
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

board = [[' ' for x in range(3)] for y in range(3)]

while True:
    print_board(board)
    # 사용자로부터 좌표를 입력받는다.
    x = int(input("다음 수의 x좌표를 입력하시오: "))
    y = int(input("다음 수의 y좌표를 입력하시오: "))
    if board[x][y] != ' ':
        print("잘못된 위치입니다. ")
        continue
    else:
        board[x][y] = 'X'
        if check_win(board, 'X'):
            print_board(board)
            print("사용자가 이겼습니다!")
            break
        if check_draw(board):
            print_board(board)
            print("무승부입니다!")
            break
    
    # 컴퓨터가 놓을 위치를 결정한다. 첫 번째로 발견하는 비어있는 칸에 놓는다.
    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ' and not done:
                board[i][j] = 'O'
                done = True
                break
        if done:
            break

    if check_win(board, 'O'):
        print_board(board)
        print("컴퓨터가 이겼습니다!")
        break
    if check_draw(board):
        print_board(board)
        print("무승부입니다!")
        break

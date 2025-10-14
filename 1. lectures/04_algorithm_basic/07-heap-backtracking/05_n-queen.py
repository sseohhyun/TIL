def is_vaild_pos(board, row, col):
    # 현재 열에 다른 퀸이 있는지 검사
    for idx in range(row): # 내 밑에는 퀸이 없으므로
        if board[idx][col] == 1 :
            return False
    # 현재 위치의 왼쪽 대각선 위로 퀸이 있는지 검사
    '''
        row = col = 2라고 가정한다면
        row, col = [2,1,0], [2,1,0]
        row, col = zip(range(row, -1, -1) , range(col, -1, -1))
        (2,2), (1,1), (0,0)
    '''
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # 현재 위치의 오른쪽 대각선 위로 퀸이 있는지 검사
    '''
        row = col = 2라고 가정한다면
        row, col = [2,1,0], [2,3,4]
        row, col = zip(range(row, -1, -1) , range(col, n))
    '''
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    # 모든 검증이 끝났는데 여기까지 왔다면
    return True # 이 위치에 퀸을 놓을 수 있음

def n_queens(row, board):
    global cnt
    cnt += 1
    # row 가 내 모든 행에 대해서 조사를 했다면...
    if row == n :
        # 어떠한 일을 하고 종료
        solutions.append([r[:] for r in board])
        return

    # 아직 모든 행에 대해서 조사 x -> 모든 열에 대해서 현재 행에 퀸을 놓아 볼 것
    for col in range(n):
        # 현재 위치에 퀸을 놓아도 되는지 판별
        if is_vaild_pos(board, row, col): # True or False 반환
            board[row][col] = 1
            n_queens(row+1, board)
            board[row][col] = 0        # 조사하러 떠났는데... 돌아왔다면, 원상복귀

n = 4
board = [[0] * n for _ in range(n)]  # 4*4 2차원 배열 생성
solutions = []  # 모든 솔루션을 저장할 리스트
cnt = 0 # 몇 번만에 완성?(함수가 호출될 때마다 +1)

# n_queens 라는 함수를 호출 하였을 때 언제까지 조사?
# 퀸 4개를 모두 놓았고, 그게 solution이라면 어떠한 일을 할 것임
    # 그러기 위해서, 퀸을 현재 조사 위치에 놓을 수 있을지도 판별
n_queens(0, board)

for solution in solutions:
    print(solution)
print(cnt)
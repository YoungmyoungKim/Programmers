def solution(board):
    width=len(board[0])
    height=len(board)
    for x in range(1, height):
        for y in range(1, width):
            if board[x][y]==1:
                board[x][y]=min(board[x-1][y-1], board[x-1][y], board[x][y-1])+1
    return max(sum(board, []))**2

b1=[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
b2=[[0,0,1,1],[1,1,1,1]]

print(solution(b1))
print(solution(b2))

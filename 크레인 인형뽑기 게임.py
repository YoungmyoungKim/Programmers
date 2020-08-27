def solution(board, moves):
    size=len(board)
    stack=[]
    for move in moves:
        for i in range(size):
            if board[i][move-1] != 0:
                stack.append(board[i][move-1])
                board[i][move-1]=0
                break
    count=0
    new_count= -1
    while True:
        if new_count == count:
            break
        new_count=count
        for i, val in enumerate(stack):
            if i !=0 and val==stack[i-1]:
                del stack[i]
                del stack[i-1]
                count+=2
                break

    return count

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]

print(solution(board, moves))

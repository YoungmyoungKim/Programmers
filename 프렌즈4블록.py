def check4Blocks(m, n, board):
    li=[]
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] != '0' and board[i][j]==board[i+1][j]==board[i][j+1]==board[i+1][j+1]:
                li.append((i, j))
                li.append((i+1, j))
                li.append((i, j+1))
                li.append((i+1, j+1))
    return list(set(li))

def solution(m, n, board):
    twistBoard=[[] for _ in range(n)]
    count=0
    for i in range(m):
        for j in range(n):
            twistBoard[j].append(board[m-i-1][j])

    while True:
        blocks=check4Blocks(n, m, twistBoard)
        blocks.sort(reverse=True)
        if len(blocks)==0:
            break
        count+=len(blocks)
        for i, j in blocks:
            del twistBoard[i][j]
            twistBoard[i].append('0')

    return count


m1, n1, board1=4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]
m2, n2, board2=6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m1, n1, board1))
print(solution(m2, n2, board2))

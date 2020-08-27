def solution(brown, red):
    for i in range(red, 0, -1):
        if red%i==0:
            j=red//i
            if (i+2)*(j+2)==brown+red:
                return [i+2, j+2]

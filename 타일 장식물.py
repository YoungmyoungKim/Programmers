def solution(N):
    f=[1, 1]
    for i in range(2, N+1):
        f.append(f[i-2]+f[i-1])
    answer=(f.pop()+f.pop())*2
    return answer

print(solution(5))
print(solution(6))

def solution(begin, target, words):
    if target not in words:
        return 0
    count=0
    #DFS 구현 필요
    while begin != target:
        if len(candidates)>0:


    return NextWords(begin, words)
#다음 바꿀 수 있는 단어 목록
def NextWords(cur_word, words):
    candidates=[]
    cur=list(cur_word)
    for word in words:
        count=0
        for i, ch in enumerate(word):
            if cur[i] != ch:
                count+=1
        if count==1:
            candidates.append(word)
    return candidates


b1, t1, words1="hit", "cog", ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
b2, t2, words2="hit", "cog", ['hot', 'dot', 'dog', 'lot', 'log']

print(solution(b1, t1, words1))
print(solution(b2, t2, words2))

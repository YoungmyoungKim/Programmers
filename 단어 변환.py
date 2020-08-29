def solution(begin, target, words):
    if target not in words:
        return 0
    stack=[(begin, 0, words)]
    while stack:
        temp=[]
        while stack:
            cur_word_info=stack.pop()
            candidates=NextWords(cur_word_info)
            temp.extend(candidates)
        for x, y, z in temp:
            if x == target:
                return y
        stack.extend(temp)
    return 0

#다음 바꿀 수 있는 단어 목록
def NextWords(cur_word_info):
    candidates=[]
    cur, cnt, words=cur_word_info[0], cur_word_info[1], cur_word_info[2]
    for word in words:
        count=0
        for c, w in zip(cur, word):
            if c!=w:
                count+=1
        if count==1:
            candidates.append((word, cnt+1, [x for x in words if x != word]))
    return candidates



b1, t1, words1="hit", "cog", ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
b2, t2, words2="hit", "cog", ['hot', 'dot', 'dog', 'lot', 'log']

print(solution(b1, t1, words1))
print(solution(b2, t2, words2))

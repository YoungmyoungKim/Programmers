def solution(n, words):
    answer = []
    for i, word in enumerate(words[1:], start=1):
        if word in words[:i] or word[0] != words[i-1][-1]:
            turn = (i+1)//n if (i+1)%n==0 else (i+1)//n+1
            person=(i+1)%n if (i+1)%n != 0 else n
            return [person, turn]

    return [0, 0]
n1, words1=3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
n2, words2=5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
"ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
n3, words3=2, ["hello", "one", "even", "never", "now", "world", "draw"]

print(solution(n1, words1))
print(solution(n2, words2))
print(solution(n3, words3))

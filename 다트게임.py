import re
def solution(dartResult):
    pattern='\d+[SDT]+[*#]?'
    points=re.findall(pattern, dartResult)
    print(points)
    scores=calScore(points)

    return sum(scores)

def calScore(points):
    scores=[]
    for point in points:
        bonus=re.findall('[SDT]', point)
        digits=re.findall('\d+', point)
        cur_score=0
        if bonus[0]=='S':
            scores.append(int(digits[0]))
        elif bonus[0]=='D':
            scores.append(int(digits[0])**2)
        elif bonus[0]=='T':
            scores.append(int(digits[0])**3)

        if '*' in point:
            scores[-1]=scores[-1]*2
            if len(scores)>1:
                scores[-2]=scores[-2]*2
        elif '#' in point:
            scores[-1]=-scores[-1]

    return scores

dart1="1S2D*3T"
dart2="1D2S#10S"
dart3="1D2S0T"
dart4="1S*2T*3S"
dart5="1D#2S*3S"
dart6="1T2D3D#"
dart7="1D2S3T*"

print(solution(dart1))
print(solution(dart2))
print(solution(dart3))
print(solution(dart4))
print(solution(dart5))
print(solution(dart6))
print(solution(dart7))

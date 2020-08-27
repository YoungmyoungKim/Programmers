import re
user_input = input()
count=0
if len(user_input)>=10:
    count+=1
if re.findall('\d+', user_input)>0:
    count+=1
print("LEVEL"+str(count))


"""

TEST[AI검색플랫폼] 머신러닝 개발자
암호 등급_A
챔피언스 리그_A
과자공장_A
전쟁2_A
TEST[AI검색플랫폼] 머신러닝 개발자
0 / 4
1:35:23
문제정보
문제정보
암호 등급_A
브루트포스 공격(Brute-force Attack)은 암호를 풀기 위해 가능한 모든 경우의 것들을 대입하는 해킹 공격 방법이다. 만약에 암호가 4자리의 숫자로만 구성되어 있다면 0000 ~ 9999까지의 가능한 모든 경우를 컴퓨터가 계산하여 대입하는데는 0.01초가 걸리지 않는다. 또한 10자리의 숫자로만 구성된 암호를 모두 시도해보는데 역시 1초가 걸리지 않는다. 이러한 브루트포스 공격에 대비하기 위해서는 가능한 암호가 만들어질 수 있는 경우의 수를 늘려야 한다. 그렇기 때문에 암호는 숫자와 영어, 특수문자 등이 섞인 짧지 않은 길이로 구성되어야 한다. 암호등급은 충족하는 규칙의 개수에 따라 정해지며, 구체적인 암호등급의 규칙은 아래와 같다.

영어 소문자를 포함한다.
영어 대문자를 포함한다.
숫자(0~9)를 포함한다.
특수문자를 포함한다.
비밀번호의 길이는 10자리 이상이다.
위 조건을 예로, "0000"은 숫자로만 구성되어있기 때문에 LEVEL1 등급이다. "Goorm2020"은 영어 대문자, 영어 소문자, 숫자를 포함 하고 있으므로 LEVEL3 등급이다. "LevelGoorm2020!@#"의 경우에는 영어 대문자, 소문자, 숫자, 특수문자를 포함하고, 비밀번호의 길이 또한 10자리를 넘게되어 LEVEL5가 된다.

이렇게 주어진 규칙에 충족하는 개수에 따라 LEVEL1~5가 정해지는데, 입력되는 문자열에 맞춰 암호등급을 출력해보자.



입력

공백이 없는 문자열이 하나 주어지는데, 이 문자열의 길이는 1 이상 100 이하이다.

문자열의 모든 문자는 영어 소문자, 대문자, 숫자(0~9), 특수문자로만 구성되고, 특수문자는 영어 소문자, 대문자, 숫자(0~9)가 아닌 모든 문자를 뜻한다.



출력

첫 번째 줄에 암호 등급을 출력한다. 충족하는 규칙에 개수에 따라 "LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4", "LEVEL5" 중 맞는 등급을 출력한다.

입/출력 예시
:
공백
:
줄바꿈
:
탭
예시 1
입력
adfkdncjdk
출력
LEVEL2
예시 2
입력
Aei0#
출력
LEVEL4
예시 3
입력
aq%~9P2!@@s!v#&&KM^lFf
출력
LEVEL5
⋇ 입출력 형식을 잘 지켜주세요
Python3
1
# -*- coding: utf-8 -*-
2
# UTF-8 encoding when using korean
3
import re
4
from collections import Counter
5
user_input = input()
6
count=0
7
if len(user_input)>=10:
8
    count+=1
9
if Counter(re.findall('\d+', user_input)>0:
10
    count+=1
11
print("LEVEL"+str(count))
12
​
실행결과
제출결과
2020 Summer Tech Internship
1/4
"""

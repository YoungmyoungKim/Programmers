"""
TEST[AI검색플랫폼] 머신러닝 개발자
암호 등급_A
챔피언스 리그_A
과자공장_A
전쟁2_A
TEST[AI검색플랫폼] 머신러닝 개발자
1 / 4
1:10:25
문제정보
문제정보
전쟁2_A
지휘관 마이클은 전쟁에서 중복된 진열을 제거하여 여러 전투를 승리로 이끌었지만 이 전략에 큰 문제점이 있다는 걸 알아챘다. 항상 같은 진열에 속한 병사들끼리 함께 훈련을 받기 때문에 전투에 참여하지 못한 진열의 병사들이 다른 진열에 합류하여 전투에 참여하려면 새롭게 훈련을 받아야 한다는 점이다.

낭비되는 훈련 비용을 막기 위해 특정 진열이 다른 진열로 전투를 할 수 있도록 훈련을 하는데 필요한 최소 비용을 구해보자!



입력

첫 번째 줄에는 일렬로 서있는 병사의 수 과 훈련 비용 정보의 개수 이 주어진다.

두 번째 줄부터 번째 줄까지 훈련 비용 정보가 한 줄에 하나씩 주어진다. 훈련 비용 정보는 의 형태로 주어지며 이는 모양의 진열이 모양의 진열이 되기위해 필요한 훈련 비용이 임을 뜻한다. 각 진열은 병사들이 서있는 위치는 o, 병사들이 서있지 않은 위치는 x로 표시된다. 훈련 비용 정보가 중복되게 주어지는 경우는 없다.

번째 줄에는 질문의 수 가 주어진다.

번째 줄부터 각 줄에는 질문이 의 형태로 주어지며 는 진열정보이다.



출력

각 줄에 진열이 진열이 되기 위해 필요한 최소 비용을 출력한다. 만약 진열을 변경할 수 없다면 을 출력한다.



풀이 예시

두 번째 예시의 각 질문은 아래와 같은 과정의 훈련을 거쳐 진열을 바꿀 수 있다.

oxo > xoo > oox

ooo > oox

xxx는 xox로 바꿀 수 있는 방법이 없다.

입/출력 예시
:
공백
:
줄바꿈
:
탭
예시 1
입력
24
oxoo4
oxxo4
xxox1
xooo3
3
xooo
ooxx
xxoo
출력
3
-1
5
예시 2
입력
39
xoooox4
oooxox4
oxxxoo5
ooxooo3
oooxxo3
xoxxoo3
oxoxoo4
ooooox4
ooooxx5
3
oxooox
ooooox
xxxxox
출력
8
4
-1
예시 3
입력
36
xxxxxo4
oxoooo5
xoooox5
xxoxox2
xoooxo4
oxoxxo1
4
xoxxoo
ooxxxo
oxxoxx
xooooo
출력
-1
-1
0
9
⋇ 입출력 형식을 잘 지켜주세요
Python3
1
# -*- coding: utf-8 -*-
2
# UTF-8 encoding when using korean
3
user_input = input()
4
print ("Hello Goorm! Your input is " + user_input)
실행결과
제출결과
2020 Summer Tech Internship
4/4
"""

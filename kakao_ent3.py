"""
TEST[AI검색플랫폼] 머신러닝 개발자
암호 등급_A
챔피언스 리그_A
과자공장_A
전쟁2_A
TEST[AI검색플랫폼] 머신러닝 개발자
1 / 4
1:11:48
문제정보
문제정보
과자공장_A
유현성 팀장은 현재 과자를 생산하는 A 공장에서 근무하고 있다. A 공장에서 유현성 팀장이 담당하는 과자는 긴 막대 과자로, 맛이 좋을 뿐만 아니라 먹는 재미가 다양하여 많은 사람들에게 사랑받고 있다.

그러던 와중 갑자기 공장에 알 수 없는 문제가 발생하여 항상 일정하던 과자의 길이가 눈에 띌 만큼 들쭉날쭉한 길이로 생산되었다. 유현성 팀장은 납품을 위해 잘못 생산된 과자가 모두 일정한 길이를 갖도록 가공하려 한다.

정리하면 현재 임의의 길이를 가진 과자들은 N개 생산되었고, 이 N개의 과자들을 모두 일정한 길이로 가공한 과자 K개로 만들고자 한다. 단, 과자의 길이를 최대한 길게 가공하려 한다.

예를 들어 2개의 과자가 잘못 생산되었는데 각 과자의 길이가 6.3, 4.3라고 가정하자. 이 2개의 과자를 가공하여 일정한 길이로 통일된 3개의 과자를 만들고자 한다. 이 경우 과자가 가질 수 있는 최대의 길이는 3.15이므로 첫 번째 과자를 절반으로 나누어 길이가 3.15인 과자가 2개를 만들고, 두번째 과자에서 1.15만큼을 잘라내어 3.15의 과자 하나를 만들 수 있다.

이렇게 임의의 길이로 잘못 생산된 과자의 개수와 그 과자의 길이들, 가공 결과 만들어내고자 하는 과자의 갯수가 주어졌을 때, 만들 수 있는 가공된 과자의 최대 길이를 구해보자.



입력
첫 줄에 N, K가 공백 구분으로 입력된다.

정수 N은 임의의 길이로 생산된 과자의 갯수이며, 정수 K는 가공이 완료되었을 때 존재해야 하는 과자의 갯수이다.

두 번째 줄부터 총 N개의 줄에 걸쳐 임의의 길이로 생산된 과자의 길이를 의미하는 실수 가 각각 주어진다.



출력
가공한 결과 나올 수 있는 과자의 최대 길이를 소숫점 세 번째 자리에서 반올림하여 두 번째 자리까지 출력한다.

입/출력 예시
:
공백
:
줄바꿈
:
탭
예시 1
입력
23
6.3
4.3
출력
3.15
예시 2
입력
18300
51.28
96.87
96.86
48.63
87.83
51.29
56.72
38.05
3.88
79.40
33.43
30.75
13.12
67.80
20.15
96.71
95.93
10.91
출력
3.20
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
3/4
"""

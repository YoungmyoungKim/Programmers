def solution(k, room_number):    #효율성 X
    room_state=[0]*(k+1)
    answer=[]
    if room_number==list(set(room_number)):
        return room_number
    for num in room_number:
        i=num
        if room_state[i] == 1 :
            while room_state[i] ==1 and i <= k:
                i+=1
        answer.append(i)
        room_state[i]=1

    return answer

import sys
sys.setrecursionlimit(1500)

def findEmptyRoom(number, rooms): # 빈방을 찾는 함수
    if number not in rooms:
        rooms[number] = number + 1
        return number

    empty = findEmptyRoom(rooms[number], rooms)
    rooms[number] = empty + 1
    return empty


def solution2(k, room_number):
    answer = []
    rooms = dict() # 몇번 방이 비어있는지 체크하는 딕셔너리

    for number in room_number:
        print(rooms)
        emptyRoom = findEmptyRoom(number, rooms)
        answer.append(emptyRoom)

    return answer

k=10
room_number=[1, 3, 4, 1, 3, 1]

print(solution2(k, room_number))

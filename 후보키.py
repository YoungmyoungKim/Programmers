from itertools import combinations
def solution(relation):
    dic=[]
    attributes=['num', 'name', 'major', 'grade']
    for i in range(len(relation[0])):
        temp={}
        temp[attributes[0]]=relation[i][0]
        temp[attributes[1]]=relation[i][1]
        temp[attributes[2]]=relation[i][2]
        temp[attributes[3]]=relation[i][3]
        dic.append(temp)
    answer=[]
    for i in range(1, len(relation[0])+1):
        if i>len(attributes):
            break
        li=list(combinations(attributes, i))
        values=[]
        for j in range(len(dic)):
            temp=()
            for val in li:
                for k in range(i):
                    temp+=(dic[j][val[k]])
            values.append(temp)
        print(values)
        print(list(set(values)))
        if leng==len(list(set(values))):
            answer.append(val)

    # 조합 내용 리스트로 만들고 set을 통해 중복제거, 원래 리스트와 길이가 같으면 후보키 가능
    return dic

relation=[["100","ryan","music","2"],["200","apeach","math","2"],
["300","tube","computer","3"],["400","con","computer","4"],
["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))

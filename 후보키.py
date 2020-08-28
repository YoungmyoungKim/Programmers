from itertools import combinations
def solution(relation):
    len_rows=len(relation)
    len_cols=len(relation[0])
    cols=range(len_cols)
    lst=[]
    for n in range(1, len_cols+1):
        comb=combinations(cols, n)
        for sel_attributes in list(comb):
            if checkCandidate(sel_attributes, len_rows, relation):
                lst.append(set(sel_attributes))
    #최소성 만족 안하면 제거
    for el1 in lst[:]:
        for el2 in lst[:]:
            if el1==el1 & el2:
                #el1&el2는 el1과 el2의 교집합
                #el1과 el1&el2가 같다는 것은 el2가 없어도 된다는것, 최소성 만족X
                if el1 != el2:
                    lst.remove(el2)
    return len(lst)
#유일성 체크
def checkCandidate(attributes, len_rows, relation):
    temp=[tuple([item[idx] for idx in attributes]) for item in relation]
    if len(set(temp)) != len_rows:
        return False
    return True
relation=[["100","ryan","music","2"],["200","apeach","math","2"],
["300","tube","computer","3"],["400","con","computer","4"],
["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))

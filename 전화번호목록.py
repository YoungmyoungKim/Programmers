def solution_1(phone_book):
    answer = True
    for i in phone_book:
        for j in phone_book[1:]:
            if i in j:
                answer=False

    return answer

def solution_2(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i==j:
                continue
            if phone_book[i] in phone_book[j]:
                answer=False

    return answer

def solution_3(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i==j:
                continue
            if phone_book[i] in phone_book[j]:
                answer=False

    return answer

def solution_4(phone_book):      #시간초과
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i==j:
                continue
            if phone_book[i]==phone_book[j][0:len(phone_book[i])]:
                answer=False
                break
    return answer

def solution_5(phone_book):     #.sort() 쓰면 런타임에러 
    phone_book=sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

phone_book_1=["119", "97674223", "1195524421"]
phone_book_2=['123', '456', '789']
phone_book_1.sort(key= lambda x : len(x) , reverse = True)

temp=[ ]

print(list(phone_book_1[0]))

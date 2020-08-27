def solution(record):
    dic_user={}
    chat=[]
    result=[]
    for user in record:
        li=user.split(" ")
        chat.append(li)
        if li[0] in ["Change", "Enter"]:
            dic_user[li[1]]=li[2]

    for val in chat:
        if val[0]=="Enter":
            result.append(dic_user[val[1]]+"님이 들어왔습니다.")
        elif val[0]=="Leave":
            result.append(dic_user[val[1]]+"님이 나갔습니다.")


    return result

record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))

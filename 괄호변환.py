def bracket_to_int(b):
    if b == '(':
        return 1
    else:
        return -1

def solution(p):
    if len(p)==0:
        #print(u, v)
        return p
    else:
        u, v=split_String(p)
        if is_RightString(u)==True:
            return str(u)+solution(v)
        else:
            res="("+solution(v)+")"
            u = ''.join(list(map(lambda x: '(' if x == ')' else ')', u)))
            """for i, s in enumerate(u):
                if s=="(":
                    u=u[:i]+")"+u[i+1:]
                else:
                    u=u[:i]+"("+u[i+1:]"""
            return res+str(u[1:-1])

def is_RightString(p):
    count=0
    for val in p:
        if count<0:
            return False
        count += bracket_to_int(val)
    return True

def split_String(p):
    count=0
    for i, val in enumerate(p):
        count += bracket_to_int(val)
        if count==0:
            return p[:i+1], p[i+1:]
    return p, ""

p1="(()())()"
p2=")("
p3="()))((()"

#print(p1[1:-1])
print(solution(p1))
print(solution(p2))
print(solution(p3))

#print(is_RightString(p1))
#print(is_RightString(p2))
#print(is_RightString(p3))

#print(split_String(p1))
#print(split_String(p2))
#print(split_String(p3))

from datetime import datetime
def solution(m, musicinfos):
    dic={'A#': 'a', 'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g'}

    for ch in dic:
        if ch in m:
            m=m.replace(ch,dic[ch])
    ans=[]
    for musicinfo in musicinfos:
        start, end, title, melody=musicinfo.split(',')
        diff=(datetime.strptime(end, "%H:%M")-datetime.strptime(start, "%H:%M")).seconds//60
        for ch in dic:
            if ch in melody:
                melody=melody.replace(ch,dic[ch])
        melody=melody*(diff//len(melody))+melody[0:diff%len(melody)]
        if m in melody:
            ans.append((title, diff))

    ans.sort(key=lambda x: -x[1])

    return "(None)" if len(ans) ==0 else ans[0][0]



m1, musicinfos1="ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
m2, musicinfos2="CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
m3, musicinfos3="ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
m4, musicinfos4="CC#BCC#BCC#BCC#BCC", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

print(solution(m1, musicinfos1))
print(solution(m2, musicinfos2))
print(solution(m3, musicinfos3))
print(solution(m4, musicinfos4))

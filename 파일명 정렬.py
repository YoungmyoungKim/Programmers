import re
def solution(files):
    split_files=[]
    HEAD=re.compile('[a-zA-Z .-]+')
    NUMBER=re.compile('\d{1,5}')
    for file in files:
        head=HEAD.match(file)
        number=NUMBER.search(file)
        split_files.append([head.group(), number.group(), file[number.end():]])

    sorted_files=sorted(split_files, key=lambda x: (x[0].lower(), int(x[1])))
    answer=[]
    for file in sorted_files:
        file=''.join(file)
        answer.append(file)
    return answer

def solution2(files):
    split_files=[]

    for file in files:
        head=re.match('[a-zA-Z .-]+', file)
        number=re.search('\d{1,5}', file)
        split_files.append([head.group(), number.group(), file[number.end():]])

    sorted_files=sorted(split_files, key=lambda x: (x[0].lower(), int(x[1])))
    answer=[]
    for file in sorted_files:
        file=''.join(file)
        answer.append(file)
    return answer

file1=['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
file2=['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']

print(solution2(file1))
print(solution2(file2))

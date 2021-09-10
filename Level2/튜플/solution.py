def solution(s):
    answer = []
    s=sorted(s[2:-2].split("},{"),key=lambda x:len(x))
    for i in range(len(s)):
        s[i]=s[i].split(',')
        for j in range(len(s[i])):
            if int(s[i][j]) not in answer:
                answer.append(int(s[i][j]))
    return answer

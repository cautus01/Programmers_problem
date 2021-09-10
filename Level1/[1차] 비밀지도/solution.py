def solution(n, arr1, arr2):
    answer = [[]*(n+1) for _ in range(n)]
    for i in range(n):
        arr1[i]=format(arr1[i],'b')
        arr2[i]=format(arr2[i],'b')
        arr1[i]=arr1[i].zfill(n)
        arr2[i]=arr2[i].zfill(n)
    for i in range(n):
        for j in range(n):
            if arr1[i][j]=='1' or arr2[i][j]=='1':
                answer[i].append('#')
            if arr1[i][j]=='0' and arr2[i][j]=='0':
                answer[i].append(' ')
    for i in range(n):
        answer[i]=''.join(answer[i])
    return answer

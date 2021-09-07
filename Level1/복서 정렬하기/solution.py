def solution(weights, head2head):
    answer = {}
    n=len(weights)
    for i in range(n):
        count,score=0,0
        score=head2head[i].count('W')/(n-head2head[i].count('N')) if n!=head2head[i].count('N') else 0
        for j in range(n):
            if head2head[i][j]=='W' and weights[i]<weights[j]:
                count+=1
        answer[i+1]=[score,count,weights[i]]
    return sorted(answer,key=lambda x:answer[x],reverse=True)

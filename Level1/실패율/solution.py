def solution(N, stages):
    answer = {}
    people=len(stages)
    for i in range(1,N+1):
        nclear=stages.count(i)
        answer[i]=nclear/people if people!=0 else 0
        people-= nclear
    answer=sorted(answer,key=lambda x:answer[x],reverse=True)
    return answer

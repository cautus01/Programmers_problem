def solution(new_id):
    answer=''
    # 1 단계
    new_id=new_id.lower()
    # 2 단계
    for i in new_id:
        if i.islower() or i.isdigit() or i in ['-','_','.']:
            answer+=i
    # 3 단계
    for i in range(len(answer)):
        answer=answer.replace('..','.')
    # 4 단계
    if answer[0]=='.':
        if len(answer)>=2:
            answer=answer[1:]
    if answer[-1]=='.':
        if len(answer)>=2:
            answer=answer[:-1]
        else:
            answer=''
    # 5 단계
    if answer=='':
        answer='a'
    # 6 단계
    if len(answer)>=16:
        answer=answer[:15]
        if answer[-1]=='.':
            answer=answer[:-1]
    # 7 단계
    while len(answer)<=2:
        answer+=answer[-1]
    return answer

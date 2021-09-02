def solution(s):
    result=[] # 결과 저장
    arr=[] # 한 단어를 저장하는 리스트
    # 단어들을 저장하는 리스트
    word=['zero','one','two','three','four','five','six','seven','eight','nine'] 
    
    for x in s: # 문자를 하나씩 확인
        if x.isdigit(): # 숫자라면 결과에 저장
            result.append(x)
        else:
            arr.append(x)
            check=''.join(arr)
            if check in word:
                a=word.index(check)
                result.append(str(a))
                arr=[]
    answer=''.join(result)
    return int(answer)

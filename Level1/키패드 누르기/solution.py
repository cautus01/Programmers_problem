def solution(numbers, hand):
    answer = ''
    phone=[(3,1),(0,0),(0,1),(0,2),
       (1,0),(1,1),(1,2),
       (2,0),(2,1),(2,2)]

    xL,yL=3,0
    xR,yR=3,2
    for num in numbers:
    # 1, 4, 7이 입력될 때 왼손
        if num in [1,4,7]:
            answer+='L'
            # 왼손 위치 바꾸기
            xL,yL=phone[num]
    # 3, 6, 9이 입력될 때 오른손
        if num in [3,6,9]:
            answer+='R'
            # 오른손 위치 바꾸기
            xR,yR=phone[num]
    # 2, 5, 8, 0이 입력될 때
        if num in [2,5,8,0]:
            x,y=phone[num]
            left=abs(x-xL)+abs(y-yL)
            right=abs(x-xR)+abs(y-yR)
            # 오른쪽 거리가 더 짧거나 (왼쪽과 오른쪽의 길이가 같고 오른손잡이면)
            if right<left or (right==left and hand=="right"):
                xR,yR=phone[num]
                answer+='R'
            # 왼쪽 거리가 더 짧거나 (왼쪽과 오른쪽의 길이가 같고 왼손잡이면)
            if right>left or (right==left and hand=="left"):
                xL,yL=phone[num]
                answer+='L'
    return answer

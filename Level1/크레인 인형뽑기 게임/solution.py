def solution(board, moves):
    basket=[]
    n=len(board)
    answer=0
    # 크레인 작동
    for i in moves:
        for j in range(n):
            # 만약 비어있지 않다면
            if board[j][i-1]!=0:
                # 바구니에 넣고
                basket.append(board[j][i-1])
                # 만약 집어넣은 값과 이전 값이 같다면
                if len(basket)>=2 and basket[-1]==basket[-2]:
                    # 리스트에서 지운다.
                    basket.pop(-1)
                    basket.pop(-1)
                    answer+=2
                # 보드를 비운다
                board[j][i-1]=0
                break
    return answer

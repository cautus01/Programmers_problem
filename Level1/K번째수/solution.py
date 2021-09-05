import copy

def solution(array, commands):
    answer = []
    for i,j,k in commands:
        test=copy.deepcopy(array)
        test=test[i-1:j]
        test.sort()
        answer.append(test[k-1])
    return answer

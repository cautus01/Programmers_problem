from itertools import permutations
import math

def prime_number(x):
    if x==0 or x==1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

def solution(numbers):
    answer=set()
    s1=set()
    for i in range(len(numbers)):
        s1.update(list(map(''.join, permutations(numbers,i+1))))
    for i in s1:
        if prime_number(int(i))==True:
            answer.add(int(i))
    return len(answer)

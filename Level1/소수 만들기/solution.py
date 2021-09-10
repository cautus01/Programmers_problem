import math
from itertools import combinations
def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

def solution(nums):
    answer = 0
    for com in combinations(nums,3):
        x,y,z=com
        number=x+y+z
        if is_prime_number(number):
            answer+=1
    return answer

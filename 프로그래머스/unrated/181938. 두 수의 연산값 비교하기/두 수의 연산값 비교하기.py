def solution(a, b):
    answer = 0
    c= str(a)+str(b)
    answer = max(int(c),2*a*b)
    return answer
def solution(binomial):
    answer = 0
    cal = binomial.split()
    
    if cal[1] == '+': answer = int(cal[0]) + int(cal[2])
    elif cal[1] == '-': answer = int(cal[0]) - int(cal[2])
    else : answer = int(cal[0]) * int(cal[2])
    
    return answer
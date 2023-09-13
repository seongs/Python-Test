def solution(n):
    answer = []
    answer.append(n)
    while (True):
        if n % 2 == 0 : 
            n = n // 2
            answer.append(n)
        elif n == 1 :
            break
        elif n % 2 == 1 :
            n = 3 * n + 1
            answer.append(n)
    
    return answer
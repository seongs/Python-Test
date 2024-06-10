def solution(n):
    odd = 1
    answer = []
    while odd <= n:
        answer.append(odd)
        odd +=2
    return answer
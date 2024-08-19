def solution(chicken):
    answer = 0
    while chicken >= 10:
        div,mode = divmod(chicken, 10)
        answer += div
        chicken = div + mode
    return answer
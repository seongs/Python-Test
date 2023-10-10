def solution(myString):
    answer = []
    answer = list(filter(None,myString.split('x')))
    answer.sort()
    return answer
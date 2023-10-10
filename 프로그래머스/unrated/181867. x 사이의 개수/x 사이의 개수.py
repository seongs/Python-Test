def solution(myString):
    answer = []
    splits = []
    splits = myString.split('x')
    for i in splits:
        answer.append(len(i))
    return answer
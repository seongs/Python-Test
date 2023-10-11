def solution(arr):
    answer = []
    i = 0
    while (i < len(arr)):
        if len(answer) == 0:
            answer.append(arr[i])
            i += 1
        elif arr[i] == answer[-1] :
            answer.pop()
            i += 1
        elif arr[i] != answer[-1] :
            answer.append(arr[i])
            i += 1
    if len(answer) == 0 : answer = [-1] 

    
    return answer
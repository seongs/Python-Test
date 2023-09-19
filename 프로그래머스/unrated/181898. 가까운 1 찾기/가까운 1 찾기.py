def solution(arr, idx):
    answer = 0
    temp = arr[idx:]
    if 1 in temp:
        answer  = temp.index(1) + idx
    else :
        answer = -1
    
    return answer
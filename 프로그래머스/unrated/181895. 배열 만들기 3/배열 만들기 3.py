def solution(arr, intervals):
    answer = []
    for start,end in intervals:
        answer.append(arr[start:end+1])
    answer = sum(answer,[])
    return answer
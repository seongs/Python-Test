def solution(arr, k):
    answer = []
    arr = [x for i, x in enumerate(arr) if x not in arr[:i]]
    if len(arr)>=k:
        answer = arr[:k]
    else:
        answer = arr [:k]
        answer += [-1] * (k-len(arr))
    return answer
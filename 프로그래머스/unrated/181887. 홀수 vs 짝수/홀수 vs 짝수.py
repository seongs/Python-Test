def solution(num_list):
    even = num_list[1::2]
    odd = num_list[::2]
    if sum(even) > sum(odd):
        return sum(even)
    elif sum(even) < sum(odd):
        return sum(odd)
    else:
        return sum(odd)
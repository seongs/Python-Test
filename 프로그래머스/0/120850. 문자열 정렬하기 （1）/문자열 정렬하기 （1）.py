def solution(my_string):
    answer = []
    return sorted([int(i) for i in my_string if i.isdigit()])
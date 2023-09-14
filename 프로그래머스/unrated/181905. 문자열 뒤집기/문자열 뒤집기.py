def solution(my_string, s, e):
    answer = ''
    mid_string = my_string[s:e+1]
    answer = my_string[:s] + mid_string[::-1] + my_string[e+1:]
    return answer
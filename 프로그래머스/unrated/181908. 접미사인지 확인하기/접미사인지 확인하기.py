def solution(my_string, is_suffix):
    answer = 0
    answer_list = []
    for i in range(len(my_string)):
        answer_list.append(my_string[i:])
    
    if is_suffix in answer_list:
        answer = 1
    else:
        answer = 0
    return answer
def solution(num_list):
    answer = -1
    
    for i in num_list:
        answer +=  1
        if i < 0:
            break
    
    if answer == len(num_list)-1:
            answer = -1
            
    
    return answer
def solution(num_list):
    squre = 0
    answer = 0
    multi = 1 
    
    for i in num_list:
        multi *= i
    
        squre = sum(num_list)**2
    
        if squre > multi:
            answer = 1
        elif squre < multi:
            answer = 0
    
    
    return answer
def solution(s):
    answer=0
    s_split = s.split()
    for i in range(len(s_split)):
        if s_split[i] == "Z":
            answer -= int(s_split[i-1])
        else:
            answer += int(s_split[i])
    return answer
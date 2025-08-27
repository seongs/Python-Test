import sys

alpabet = sys.stdin.readline().strip().upper()
alpabet_list = list(set(alpabet))
result=[]
for i in alpabet_list:
    result.append(alpabet.count(i))

if result.count(max(result)) > 1:
    print("?")
else:
    print(alpabet_list[result.index(max(result))])
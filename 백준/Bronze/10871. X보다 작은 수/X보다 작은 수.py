import sys
N,X = map(int,sys.stdin.readline().split())
temp1 = list(map(int,sys.stdin.readline().split()))
temp2 = []
for i in range(len(temp1)):
    if X > temp1[i]: temp2.append(temp1[i])   
    

print(' '.join(map(str,temp2)))
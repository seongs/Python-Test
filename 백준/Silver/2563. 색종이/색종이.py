import sys

paper = [[0] * 100 for _ in range(100)]

N = int(sys.stdin.readline())
for _ in range(N):
    row,col = map(int,sys.stdin.readline().split())
    for i in range(row,row+10):
        for j in range(col,col+10):
            paper[i][j] = 1


result = 0 
for k in paper:
    result+= sum(k)

print(result)

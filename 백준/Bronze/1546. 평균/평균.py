import sys

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
M = max(score)
for i in range(N): score[i] = score[i] / M * 100

print(sum(score)/len(score))
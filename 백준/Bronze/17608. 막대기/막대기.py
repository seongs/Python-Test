import sys

input = sys.stdin.readline

N = int(input())
bar = 1
h =[]
for _ in range(N):
    h.append(int(input()))
max_bar = h[-1]

for i in reversed(range(N)):
    if h[i] > max_bar:
        bar += 1
        max_bar = h[i]

print(bar)
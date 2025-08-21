import sys

remain = []

for _ in range(10):
    n = int(sys.stdin.readline())
    remain.append(n%42)

print(len(set(remain)))

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    test = sys.stdin.readline().strip()
    print(test[0]+test[-1])
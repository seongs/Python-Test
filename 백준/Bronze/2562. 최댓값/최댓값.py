import sys
num = [int(sys.stdin.readline()) for _ in range(9)]
max_num=max(num)
print(max_num)
print(num.index(max_num)+1)
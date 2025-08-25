import sys
math = list(sys.stdin.readline().split())
math[0] = math[0][::-1]
math[1] = math[1][::-1]
print(max(math))
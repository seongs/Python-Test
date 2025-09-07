import sys

N, B = map(int,sys.stdin.readline().split())
result = []

while N > 0:
    remainder = N % B
    if remainder >= 10:
        result.append(chr(remainder + 55))
    else:
        result.append(str(remainder))
    N //=B

print(''.join(reversed(result)))
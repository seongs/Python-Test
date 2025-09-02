import sys

N, B = sys.stdin.readline().split()
result = 0
B =int(B)
for i, digit in enumerate(reversed(N)):
    if digit.isdigit():
        result += int(digit) * (B**i)
    else:
        result += (ord(digit) -55) * (B**i)

print(result)
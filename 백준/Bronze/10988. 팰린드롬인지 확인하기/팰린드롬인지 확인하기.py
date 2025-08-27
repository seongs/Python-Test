import sys

voc = sys.stdin.readline().strip()
result = 0
if voc == voc[::-1]: result = 1
print(result)
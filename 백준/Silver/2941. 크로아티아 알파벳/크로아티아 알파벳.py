import sys

cloatia_alpabet = ["c=","c-","dz=","d-","lj","nj","s=","z="]
alpabet = sys.stdin.readline().strip()
cnt = 0

for i in cloatia_alpabet:
    alpabet = alpabet.replace(i,'a')

print(len(alpabet))

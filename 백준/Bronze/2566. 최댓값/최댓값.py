import sys
num=[]
for _ in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    num.append(row)

max_num = 0
max_col = 0
max_row = 0

for row in range(9):
    for col in range(9):
        if num[row][col] > max_num:
            max_num = num[row][col]
            max_row = row
            max_col = col
print(max_num)
print(max_row+1,max_col+1)
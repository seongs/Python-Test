A, B = map(int, input().split())

num=[]

for i in range(1,1000):
    for _ in range(i):
        num.append(i)

where = num[A-1:B]

print(sum(where))
N = int(input())
max_count=0
list_count=[]
evolution=0
K=0
M=0
for _ in range(N) :
    name = input()
    K,M = input().split()
    count=0

    while int(M)>=int(K):
        evolution+=1
        M=int(M)-int(K)+2
        count+=1
        if count > max_count:
            max_count=count
            max_name=name



print(evolution)
print(max_name)
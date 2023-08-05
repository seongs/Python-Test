A=[]
B=[]

A, B = input().split()

A= list(map(int,A))
B= list(map(int,B))

sum=0

for i in A :
    for j in B :
        sum+=i*j
        
print(sum)
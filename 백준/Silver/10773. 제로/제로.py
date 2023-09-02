K=int(input())

account=[]

modified_account = []


for _ in range(K):
    account.append(int(input()))

for i in account:
    if i == 0:
        del modified_account[i-1]
    else:
        modified_account.append(i)


print(sum(modified_account))
X=int(input())

X_binary = bin(X)

X_list = list(X_binary)

print(X_list.count('1'))
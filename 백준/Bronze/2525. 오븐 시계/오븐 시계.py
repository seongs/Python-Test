hour,min= map(int,input().split())
add = int(input())

print((hour+int((min+add)/60))%24,(min+add)%60)
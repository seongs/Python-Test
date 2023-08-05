Num=0
while True:
    L,P,V = map(int, input().split())
    if L ==0 and P ==0 and V==0:
        break
    date = V//P * L + min((V % P),L)
    Num += 1
    print(f"Case {Num}: {date}")
N,M = map(int,input().split())
card = list(map(int,input().split()))
Max_card =0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if M >= card[i] + card[j] + card[k] :
                Max_card = max(Max_card,  card[i] + card[j] + card[k])
                
print(Max_card)
song = ['baby','sukhwan','tururu','turu','very','cute','tururu','turu','in' ,'bed' ,'tururu', 'turu','baby','sukhwan']

N = int(input())

ru_count = N // 14

if N <= 14:
    print(song[N-1])
else:
    word = song[N % 14 - 1]
    
    if word == 'tururu' or word == 'turu':
        ru_count += 1  
        if word == 'tururu':
            ru_count += 1  
            
        if ru_count >= 5:  
            print(f'tu+ru*{ru_count}')
        else:
            print('tu' + 'ru' * ru_count)
    else:
        print(word)


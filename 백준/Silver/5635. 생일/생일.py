n = int(input())

max_yyyy=9999
max_mm=99
max_dd=99
min_yyyy=0
min_mm=0
min_dd=0

for _ in range(n):
    name,dd,mm,yyyy = input().split()
    if int(yyyy) < max_yyyy:
        max_yyyy=int(yyyy)
        max_mm=int(mm)
        max_dd=int(dd)
        max_name=name
    elif int(yyyy) == max_yyyy:
        if int(mm) < max_mm:
           max_yyyy=int(yyyy)
           max_mm=int(mm)
           max_dd=int(dd)
           max_name=name
        elif int(mm) == max_mm:
            if int(dd) < max_dd:
                max_yyyy=int(yyyy)
                max_mm=int(mm)
                max_dd=int(dd)
                max_name=name
    if int(yyyy) > min_yyyy:
        min_yyyy=int(yyyy)
        min_mm=int(mm)
        min_dd=int(dd)
        min_name=name
    elif int(yyyy) == min_yyyy:
        if int(mm) > min_mm:
           min_yyyy=int(yyyy)
           min_mm=int(mm)
           min_dd=int(dd)
           min_name=name
        elif int(mm) == min_mm:
            if int(dd) > min_dd:
                min_yyyy=int(yyyy)
                min_mm=int(mm)
                min_dd=int(dd)
                min_name=name
   
        
print(min_name)        
print(max_name)
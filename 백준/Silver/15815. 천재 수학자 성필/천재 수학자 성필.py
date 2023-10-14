
cal = list(input())
num = []

for i in cal:
    if i == '+':
        num1 = num.pop()
        num2 = num.pop()
        num.append(num1+num2)
    elif i == '-':
        num1 = num.pop()
        num2 = num.pop()
        num.append(num2-num1)
    elif i == '*':
        num1 = num.pop()
        num2 = num.pop()
        num.append(num1*num2)    
    elif i == '/':
        num1 = num.pop()
        num2 = num.pop()
        num.append(num2//num1)  
    else :
        num.append(int(i))

print(*num)
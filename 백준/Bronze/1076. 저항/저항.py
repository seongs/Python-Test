resist = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

color1= input()
color2= input()
color3= input()

color1_index=str(resist.index(color1))
color2_index=str(resist.index(color2))
color3_index=resist.index(color3)

print(int(color1_index+color2_index)*10**color3_index)
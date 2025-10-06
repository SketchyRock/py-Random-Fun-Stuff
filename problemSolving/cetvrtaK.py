xy1 = input().split()
xy2 = input().split()
xy3 = input().split()
xy4 = []

if(int(xy1[0]) != int(xy2[0])):
    xy4.append(int(xy1[0]) + int(xy2[0]) - int(xy3[0]))
else:
    xy4.append(int(xy1[0]) + int(xy3[0]) - int(xy2[0]))
    
if(int(xy1[1]) != int(xy2[1])):
    xy4.append(int(xy1[1]) + int(xy2[1]) - int(xy3[1]))
else:
    xy4.append(int(xy1[1]) + int(xy3[1]) - int(xy2[1]))
    
print(f"{xy4[0]} {xy4[1]}")
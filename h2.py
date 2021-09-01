initstate = [(1,1,1),(1,2,2),(1,3,3),(2,1,8),(2,2,0),(2,3,4),(3,1,7),(3,2,6),(3,3,5)]
goalstate = [(1,1,8),(1,2,1),(1,3,2),(2,1,3),(2,2,6),(2,3,4),(3,1,0),(3,2,7),(3,3,5)]
cnt = 0
i=0
while(i<=8):
    if initstate[i][2]==0:
        continue
    val=goalstate[i][2]
    row=goalstate[i][0]
    col=goalstate[i][1]
    for j in range(9):
        if val==initstate[j][2]:
            if col1==initstate[j][1] and row1==initstate[j][0]:
                cnt=cnt+0
                
            elif col==initstate[j][1]:
                cnt =cnt+abs(row-initstate[j][0])
                
            elif row==initstate[j][0]:
                cnt=cnt+abs(col-initstate[j][1])
                
            else :
                cnt=cnt+abs(row-initstate[j][0])+abs(col-initstate[j][1])
                
print(cnt)

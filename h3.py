queens=[(1,6,1),(2,1,2),(3,5,3),(4,7,4),(5,4,5),(6,3,6),(7,8,7),(8,1,8)]
print("The Value of H3")
i=0
cnt=0
while(i<=7):
    row=queens[i][1]
    col=queens[i][2]

    for j in range (8):
        if((queens[j][1]>row or queens[j][1]<row)and queens[j][2]==col):
            cnt=cnt+1
           
    for m in range (8):
        if(queens[m][2]>col and(queens[m][1]==row)):
            cnt=cnt+1

    for n in range (8):
        if(queens[n][1]==queens[n][2]):
            cnt=cnt+1
print(cnt)

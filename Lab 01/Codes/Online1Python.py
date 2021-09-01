tupleList1=[('child', 'Rakib', 'Hasib'),('child', 'Sohel', 'Rakib'),('child', 'Rebeka', 'Rakib'),('child', 'Hasib', 'Rashid')]

# Procedure to find the grandchildren of X

X=str(input("Grandchildren:"))
print('Grandparent:', end=' ')
i=0
while(i<=3):
    if ((tupleList1[i][0] == 'child')&( tupleList1[i][1] == X)):
        for j in range(4):
            if ((tupleList1[j][0] == 'child') & ( tupleList1[i][2] == tupleList1[j][1])):
                print(tupleList1[j][2], end=' ')   
    i=i+1  

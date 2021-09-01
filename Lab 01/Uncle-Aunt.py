tupleList1=[('parent', 'Hasib', 'Rakib','male'),('parent', 'Hasib', 'Sakib','male'),('parent', 'Rakib', 'Rebeka','female'),('parent', 'Rakib', 'Sohel','male')

X=str(input("Name:"))

i=0
            
while(i<=3):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
       Y=tupleList1[i][1]
    i=i+1
            
print('Uncle/Aunt:', end=' ')
            
m=0
while(m<=3):
    if ((tupleList1[m][0] == 'parent')&( tupleList1[m][2] == Y)):
        for j in range(4):
            if ((tupleList1[j][0] == 'parent') & ( tupleList1[m][1] == tupleList1[j][1])&( tupleList1[m][3] == 'male')):
                print(tupleList1[j][2], end=' Uncle')
            elif ((tupleList1[j][0] == 'parent') & ( tupleList1[m][1] == tupleList1[j][1])&( tupleList1[m][3] == 'female')):
                print(tupleList1[j][2], end=' Aunt')
    m=m+1














  

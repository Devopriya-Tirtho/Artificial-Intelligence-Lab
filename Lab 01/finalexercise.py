tupleList1=[('parent', 'Hasib', 'Rakib','male'),('parent', 'Hasib', 'Sakib','male'),('parent', 'Rakib', 'Rebeka','female'),('parent', 'Rakib', 'Sohel','male')]

             

X=str(input("Name:"))
print('Brother/Sister:', end=' ')
i=0
while(i<=3):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(4):
            if ((tupleList1[j][0] == 'parent') & ( tupleList1[i][1] == tupleList1[j][1])&( tupleList1[j][3] == 'male')):
                print(tupleList1[j][2], end=' Brother ')
            elif ((tupleList1[j][0] == 'parent') & ( tupleList1[i][1] == tupleList1[j][1])&( tupleList1[j][3] == 'female')):
                print(tupleList1[j][2], end=' Sister ')
     
    i=i+1




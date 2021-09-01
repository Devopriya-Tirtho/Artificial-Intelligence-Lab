myInfo = [(1,1,1),
          (1,2,2),
          (1,3,3),
          (2,1,8),
          (2,2,0),
          (2,3,4),
          (3,1,7),
          (3,2,6),
          (3,3,5)
          ]
myData = [(1,1,8),
          (1,2,1),
          (1,3,2),
          (2,1,3),
          (2,2,6),
          (2,3,4),
          (3,1,0),
          (3,2,7),
          (3,3,5)
          ]
cnt = 0;  
for i in range(9):
    if myData[i][2] is 0:
        continue
    storeValue = myData[i][2]
    storeFirst = myData[i][0]
    storeSecond = myData[i][1]
    for j in range(9):
        if storeValue == myInfo[j][2]:
            if storeSecond == myInfo[j][1] and storeFirst == myInfo[j][0]:
                cnt = cnt + 0
            elif storeSecond == myInfo[j][1]:
                cnt = cnt + abs(storeFirst - myInfo[j][0])
            elif storeFirst == myInfo[j][0]:
                cnt = cnt + abs(storeSecond - myInfo[j][1])
            else :
                cnt = cnt + abs(storeFirst - myInfo[j][0])
                cnt = cnt + abs(storeSecond - myInfo[j][1])
print(cnt)Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

def fssum():
    a=int(input("Start:"))
    d=int(input("Interval:"))
    n=int(input("Input:"))
    i,s=1,0
    while(i<=n):
        s=s+a+d*(i-1)
        i=i+1
        print("Sum:",s)
        input("Press Enter to Continue")
t=int(input("how many times?"))
for i in range (t):
    print("Iteration:",i+1)
    fssum()

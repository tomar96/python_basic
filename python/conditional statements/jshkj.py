
while True:
    n=int(input("Enter the value of n:"))
    for i in range(0,n):
        
        for i in range(0,n):
            for j in range(0,i):
                print("*",end=" ")
            print("\r")
        for i in range(0,n):
            for j in range(i,n):
                print("*",end=" ")
            print("\r")
       



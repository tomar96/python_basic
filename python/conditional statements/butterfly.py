

while True:
    n=int(input("enter the no. of n :"))
    for i in range(1,n+1):
        print("*"*i,end=" ")
        print(" "*(n-i)*2,end=" ")
        print("*"*i)
    for i in range(n,0,-1):
        print("*"*i,end=" ")
        print(" "*(n-i)*2,end=" ")
        print("*"*i);
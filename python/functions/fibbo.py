n=int(input("Enter the number of your series:"))
a=0;
b=1;
print(a)
print(b)
for i in range(1,n):
   c=a+b;
   a=b
   b=c
   print(c)



def sumofnatural(n):
    if n==0:
        return 0
    return n + sumofnatural(n-1)

g=3
f= sumofnatural(g)
print("the sum is ,"  +  str(f))
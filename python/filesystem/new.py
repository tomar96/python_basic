f=open('poem.txt')
t=f.read()
if 'twinkleee' in t:
    print("it is present")
else:
    print("not present")
f.close()

while True:
        x=input("please tell me your name ?\n")
        f=open('poem.txt','r')
        data=f.read()
        if x in data:
            print("welcome to my world\n")
        else:
            print("wrong password,")
            print("please try again.\n")
            
def locked():
    pass;
    
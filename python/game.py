
comp= input("computer:enter your choice ")

you=input("Your choice:enter your choice ")

def gamewin(comp,you):
        if comp==you:
            return None
        elif comp== 's':
            if you== 'g':
                return True
            elif you== 'w':
                return False
        elif comp== 'w':
            if you== 's':
                return True
            elif you== 'g':
                return False
        elif comp== 'g':
            if you== 'w':
                return True
            elif you== 's':
                return False
    

a=gamewin(comp,you)
print(f"comp chose  :{comp}")
print(f"you chose  :{you}")
if a== None:
            print("game tie")
elif a:
            print("you win :)")
else:
            print("you loss!")
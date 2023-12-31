n=int(input("enter the no. of words which you want to be fatch: "))
for i in range (0,n):
            
        mydicy={
            "pankha":"fan",
            "dabba":"box",
            "bastu":"things"
        }
        print("options are ",mydicy.keys())
        a=input("enter thr hindi word:\n")
        print("the meaning of this word is: ",mydicy.get(a))
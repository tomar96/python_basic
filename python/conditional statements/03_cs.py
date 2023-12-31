while True:


    a1=int(input("Enter the marks 1:"))
    a2=int(input("Enter the marks 2:"))
    a3=int(input("Enter the marks 3:"))

    if (a1<33 or a2<33 or a3<33):
        print("you are fail duo to 33 marks.")
    elif(a1+a2+a3)/3<40:
        print("you are fail duo to 40% marks.")
    else:
        print("you are pass.\n THANK YOU")
    print("\n")
    print("Thank you.")
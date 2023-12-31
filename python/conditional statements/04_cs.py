


text= input("Enter the text:\n")

if ("a boy" in text):
    spam=True
elif("click it" in text):
    spam=True
elif("good bro" in text):
    spam=True
else:
    spam=False


if (spam):
    print("It is spamming.")
else:
    print("It is not spamming.")

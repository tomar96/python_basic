def remove_and_strip(string,word):
    newstr=string.replace(word, "")
    return newstr

this= "    Hi, i am aakanshu tomar.     "
f=remove_and_strip(this,"hi")
print(f)
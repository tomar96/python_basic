from re import U
from turtle import update


first={
    "fast":"in a quick manner.",
    "jaat":"a power brand.",
    "another" : {'aakams':'player'} ,
    1:2
    }
print(list(first.keys()))
print(list(first.values()))
print(first.items())
updatefirst={
    "bhole":"hello"
}
first.update(updatefirst)
print(first)
print(first.get("fas"))
print(first["fast"])

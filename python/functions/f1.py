def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p
marks1=[50,36,26,99]
percentage1=percent(marks1)

marks2=[36,65,89,66]
percentage2=percent(marks2)


print(percentage1,percentage2)
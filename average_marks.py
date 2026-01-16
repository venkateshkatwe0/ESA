import os
mark1=int(input("Enter marks of marks 1: "))
mark2=int(input("Enter marks of marks 2: "))
mark3=int(input("Enter marks of marks 3: "))
average=(mark1+mark2+mark3)/3
if average>=90:
    print("Grade: S")
elif average>=75:
    print("Grade: A")
elif average>=60:
    print("Grade: B")
elif average>=50:
    print("Grade: C")
elif average>=35:
    print("Grade: D")
else:
    print("Grade: F")
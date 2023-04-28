avg=70

if avg >= 70:
    print("A")
elif avg>=60 and avg<70:
    print("B")
elif avg>=50 and avg<60:
    print("C")
elif avg>=40 and avg<50:
    print("D")
else:
    print("E")



a=input("Enter the first number:")
b=input("Enter second number:")
c=input("Enter the third number:")
 
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)
else:
    print("No winner")

try:
    marks=int(input("Enter marks:"))

    if marks<0 and marks>100:
        print("Invalid marks")
    else:
        if marks>=70:
            print("A")
        else:
            if marks>=60 and marks<70:
                print("B")
            else:
                if marks >=50 and marks <60:
                    print("c")
                else:
                    if marks>=40 and marks<50:
                        print("D")
                    else:
                        print("E")
except:
    print("Ensure what you have entered is a number")




#a=int(input("Enter the height: "))
#b=int(input("Enter the base: "))
#area=0.5*a*b
#print(area)

#a=int(input("Enter the number:"))
#if a%2==0:
 #   print("then number is even")
#else:
#    print("The number is odd")

#a=input("Enter your number:")
#if a[0:4]== "+254":
 #   print(a)
#elif a[0:3]=="254":
#        print("+" + a)
#elif a[0:2]=="07" or "01":
#        print("+254" + a[1:])
#elif a[0:1]=="7":
#      print("+254" + a)

    
#else:
#        if a[0:3]== "254":
#            print("+254" +a[3:])
#        else:
#                if a[0:2]== "07" or "01":
#                    print("+254" +a[1:])
#                else:
#                        if a== "71":
#                            print("+254" + a)
#                        else:
#                                print("number is null")
#entries=4
#password="admin@123"
#for enteries in range(0,4):
#  password=input("Enter your password:")
#  if password != "admin@123":
#      print("wrong password try again")
#password = "admin@123"
#count = 0
#max_attempts = 4

#while count < max_attempts:
    #user_password = input("Please enter your password: ")
   # if user_password == password:
   #     print("login succesful!")
   #     break
  #  else:
   #     count += 1
  #      if count == max_attempts:
 #           print("Account Blocked")
       



#marks=float(input("enter the marks:"))
#if marks<0 and marks>100:
 # print("invalid  marks")
#else:
    #  if marks>79:
   #     print("A")
  #    elif marks>60 and marks<=79:
    #    print("B")
   #   elif marks>49 and marks<=60:
  #      print("C")
 #     elif marks>=40 and marks<=49:
#        print("D")
  #    else:
 #       print("E")



  #speed=int(input("Enter the speed:"))
  #speed_limit=70
  #maximum=(speed-speed_limit)/5

  #if speed < 70:
   # print("OK")
  #elif (maximum) > 12:
   # print("lincence suspended")
  #else:
   #   print(maximum)


#user=int(input("enter the number:"))
#for i in range(user + 1):
 # print('*' * i)

#products=[["omo","kshs30",300],["milk","50kshs",200],["bread","45kshs",359],["coffee","5kshs",79]]
#ls1=products[0][2]
#ls2=products[1][2]
#ls3=products[2][2]
#ls4=products[3][2]
#total=ls1+ls2+ls3+ls4
#print(total)

#products=[["omo","kshs30",300],["milk","50kshs",200],["bread","45kshs",359],["coffee","5kshs",79]]
#a=0
#for i in products:
 # total=i
  #print(total)


#import datetime

#birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
#birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d").date()

#today = datetime.date.today()
#age_years = today.year - birthdate.year
#age_months = today.month - birthdate.month
#age_days = today.day - birthdate.day

#if age_months < 0 or (age_months == 0 and age_days < 0):
#    age_years -= 1
#    age_months += 12
#if age_days < 0:
#    age_days += 30  # Assuming every month has 30 days

#print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

#for i in range(0,10):
##  try:
 #   number1= float(input("enter your number:"))
  #  number2= float(input("enter your number:"))
  #  total=number1+number2
   # print(total)
    #break
  #except:
   #     print("You entered an invalid number")
      
      

#basic_salary=input("Enter the basic salary:")
#benefits=input("enter the benefits")
#gross_income=basic_salary+benefits

#if gross_income<6000:
#  print("your nhif is 120")
#elif gross_income>=6000 and gross_income<8000:
#  print("your nhif is 150")
#elif gross_income>=8000 and

#num = int(input("Enter a number: ")) # prompt user to enter a number and convert it to an integer

#for i in range(0,num): # iterate over the range of the input number
# for j in range(0, i + 1):
#    print("*", end="") # print a star without a newline character
#    print()

#def calculate(x,y):
#  total=x + y
#  return total

#t=calculate(100,102)
#print(t)




def gross_salary(i, b):
    gross_income=i + b
    return gross_income

def nssf(ti):
    nssf=ti * 0.06
    return nssf

def nhif(gross_income):
    nhif= 0
    if gross_income <= 5999:
       nhif=150
    elif gross_income >=6000 and gross_income < 7999:
       nhif = 300
    elif gross_income >= 8000 and gross_income < 11999:
        nhif = 400
    elif gross_income >= 12000 and gross_income < 14999:
       nhif = 500
    elif gross_income >= 15000 and gross_income < 19999:
       nhif = 600
    elif gross_income >= 20000 and gross_income < 24999:
        nhif = 750
    elif gross_income >= 25000 and gross_income < 29999:
         nhif = 850
    else:
        nhif = 1050
    return nhif

def payee(payee):
  payee=(10/100)*



income=float(input("Enter the basic salary :"))
benefits=float(input("Benefits :"))

g=gross_salary(income, benefits)
nssf=nssf(g)
nhif=nhif(g)
print(g)
print(nssf)
print(nhif)


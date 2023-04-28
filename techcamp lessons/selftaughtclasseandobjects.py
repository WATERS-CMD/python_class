#create a class that fills the names, ages and telephone numbers of people as shown below
#james 34 254786989098
#john 13 254768865546
#mary 46 254765569876

class Person:
  def __init__(self, name, age, telephone):
   self.name = name
   self.age=age
   self.telephone=telephone



p1=Person("james", 34, "25478989098")

p2=Person("john", 13, "254768865546")

p3=Person("mary", 46, "254765569876")

print("Hello, my name is " , p1.name.upper())
print("My age is " ,p1.age , "years")
print("my telephone contact is " ,p1.telephone)

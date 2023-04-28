side=input("enter the side: ")
class Cube():
    length=0
    def __init__(self,side):
        self.length=side
        
    def area(self):
        return self.side**2

    def volume(self):
        return self.side**3


    myname="ismail mahruf"
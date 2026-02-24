#object intanation
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("danaiel",23,"vja")
a.display()
b=Details()
b.data("bharath",24,"vja")
b.display()'''

'''#object initialization
class Details():
    #creating a constructor
    def __init__ (self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("ram",23,"vja")
a.display()'''

#runtime            
class Details():
    #creating a constructor
    def __init__ (self):
        self.name=(input("name"))
        self.age=int(input("age"))
        self.place=(input("place"))
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
a.display()




















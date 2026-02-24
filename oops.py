#oops SYNTAX
'''class classname():
    name="ram"
    age=23
    palce="vja"
    def fname(self):
        print(statements....)
a=classname()
a.fname()'''

#class declaration
class Details():
    name="ram"
    age=23
    city="gntr"
    def display(self):
        print(self.name,self.age,self.city)
a=Details()
print(dir(a))
a.display()

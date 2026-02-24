#super
#*The super function is used to methods from the parents base class inside a child derived class it helps in method overriding constructer and
#**avoid directly using the parent class name
class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child constructor")
obj1=child("ram",23)
print(obj1.name)
print(obj1.age)

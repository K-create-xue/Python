

# class Person(object):
#     def __init__(self,name,age):
#          self.name=name
#          self.age=age
#     def eat(self):
#         print("i am %s"%(self.name))
    
# class Car(object):
#     def __init__(self,brand,xinhao):
#         self.brand=brand
#         self.xinhao=xinhao
#     def run(self):
#         print("i am %s ,xinhao is %s"%(self.brand,self.xinhao))


# p1=Person("K",22)
# p1.eat()

# p2=Car() 
# p2.run() 


class User(object):

    __data=None

    def __new__(cls,*args,**kwargs):
        if not cls.__data:
            cls.__data=super(User,cls).__new__(cls,*args,**kwargs)
        return cls.__data
    
    def __init__(self,name):
        self.name=name

    def share_user(cls):
        return User
    
    
            

    




# class parent(object):
#     def __init__(self,name):
#         print("parent init")
#     def fun():
#         print("11111111111")

#     def __del__(self):
#         print("parent del")

# class child(parent):
#     def __init__(self,age):
#         # super().__init__(name)
#         self.age=age
#         print("child init")
#     def fun2(self):
#         print("22222222222222")
#     def __del__(self):
#         print("child del")


# p1=child(12)
# p1.fun2()


         
class Person(object):
    def __init__(self,name):
        self.name=name

p1=Person("K")
p1.age=19
p1.asd="asd"

print(p1.name)
print(p1.age)

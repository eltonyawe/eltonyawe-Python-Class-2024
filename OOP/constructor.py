#without parameters
class Person:
    def __init__(self):
        self.name= "Unknown"
        self.age = 0
        

#with parameter no arguements
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

print('hello')        
        
object1 = Person("Elton",22)
print(f"Name : {object1.name} \nAge : {object1.age}")  


#with default parameters and arguements
class Person:
    def __init__(self,name="Joseph",age=45):
        self.name = name
        self.age = age
        
object1 = Person()
print(f"Name : {object1.name} \nAge : {object1.age}") 


#A constructor with no parameters
class Person2:
    params = "Constructor has no params"        
      
# an instance of  class person      
obj = Person2()
print(obj.params)



    
    
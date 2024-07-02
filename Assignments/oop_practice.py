class Car:                              #Base class
    
    def __init__(self,model,colour):    #constructor (initializier) it draws real world objects in code
        self.model =model               #Atrributes,Properties
        self.colour=colour




car001 =Car("BMW","Black")#Object1
car002 =Car("Mustang","Orange")#Object2
print('Oject_1 car001 is created..')
print(f"Model : {car001.model}  \n Colour : {car001.colour}") 
print('Oject_2 car002 is created..')
print(f"Model : {car002.model}  \nColour : {car002.colour}") 
        
        
        
        
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
#Methods of an an obect (things an obect does)        
    def walk(self):
        return ("Animal walking..... through the park")

    def sit(self):
        return ("Animal sitting down on the ground...")    
    
    
    
       
            
    
animal_one = Animal("Zebra", 8)

print(f"Name of animal :{animal_one.name}\nAction of animal :{animal_one.sit()}")
def greet () :
    print("Hi")
    print ("You are Welcome to our website")
    
    
greet()    

#Function Definiton & calling Function with Arguements
def profile(name,age,course) :  #these are function_parameters
    print(f"Name : {name}, Age : {age}, Course : {course}")
    print ("You are Welcome to Greenbridge School of Technologies")
    print("Thank You .....")
    
profile("Elton",23,"Python")    #These are function_arguements
profile("Samson", 21,"Java & Python")  
profile("Yaseen",25,"Python")  
profile("Martha",20,"Python") 
profile("Tonny",33,"Python")  
   

#Function Definition of My Profile with return
def pro(name,course) :
    print(f"Name : {name},  Course : {course}")
    print ("You are Welcome to Greenbridge School of Technologies")
    print("Thank You .....")
    return name  +  course

profile= pro(" Elton" ,"  Python Programming")
print(profile)


#Function Definition of my Invoice
def invoice (name,amount,date,):
    print("Previous Debt Still Owning")
    print (f"Your Name:{name},you have a debt of ${amount:.2f},which is due by :{date},") 
    print("For more information cotact us on 0774935567")    
invoice("Yawe Elton", 1050, "1/August/2024")  


 
#Calling a Function Within a Function Using For loop

def first_name():
    first_name = "Yawe"
    for letter in first_name:
        print(letter)
first_name()

def last_name():
    last_name= "Elton"
    for num in last_name:
        print(num)
        first_name()
first_name()
last_name()
                
       


#Continue in For Loop
for number in range(1,21):
    if number == 10:
        continue
    else:
        print(number)
        
        
#Break in For Loop
for x in range(1,100):
    if x == 11:
        break
    else:
        print(x)       


#Calling a Function Within a Function Using For loop
def sum():
    print("end of year results")
    print("you passed,"'elton')
sum()    


def greet(Name) :
    print("hi there ")
    print('Welcome,'+ Name)
    
greet("Elton")    
greet("Samsom")  
greet("Yaseen")  
greet("Tonny")


def sum(Students_passed):
    print("end of year results")
    print("Those who passed,"+ Students_passed)
sum("Students_passed")  
sum("samson_passed")
sum("yaseen_passed")
sum('tonny_passed')  
sum("yawe_passed")




 
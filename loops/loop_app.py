#FOR LOOP

def fun1():
    characters = "Python"
    for character in characters:
        print(character)
        
        
fun1()


def fun1():
    characters = "Python"
    for character in characters:
        print(character)
          
def fun2():
    characters = "Programming"
    for x in characters:
        print(x)

fun1()        
fun2() 

          
#Iterating Using Seqeunce  {lists,tuple,sets,dict}
numbers =(1,2,3,4,5,6,7,8,9,10,11)
for number in numbers :
    print(number)


# Numbers are Iterated 1-20" using Range.
for digit in range(1,11):
    print(digit)
    


#Number are Reversed from big to small "10-1"
for num in reversed(range(1,11)):
    print(num)
    
    

#Ranging Number by sequence "3" when iterating.
for num in range(1,21,3):
    print(num)
    
    

#Iterating Using Strings.
visa_card = "1234-5678-3456-6645"
for each_number in visa_card :
    print(each_number)
print("Success!!!")    

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
last_name()
        
              
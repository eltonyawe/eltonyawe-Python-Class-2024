Grade = int(input("Grade"))

def Grade (Grade):
    match Grade :
        case Grade if (Grade <= 80):
            print("A ")
        
        case Grade if (Grade <= 79):
            print("B")  
            
        case Grade if(Grade <= 70):
            print("C")
        case _:
            print("Failure")
m= int(input("Grade"))

Grade(m)              

        
        

    
 



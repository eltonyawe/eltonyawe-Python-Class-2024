dict1={'a':1, 'b':20, 'c':3}
dict1['b']
print(dict1)

del dict1['a']
print(dict1)

dict1.update({'a':10})
print(dict1)

get_dict4 = {'Name' : 'Yawe Elton','Age' : '23','Status' : 'Single & Searching'}
print (get_dict4)
get_dict4.update({'DOB' : 2002})
print (get_dict4)


cars = {'model' : 'toyota','price' : 45000000}
print (cars)

for vech in cars :
    print(vech)

print(cars)

cars.update({'tax' : 15 })
print(cars)


food = {'rice' : 4000,'posho' : 2500}
print (food)

for eats in food :
    print(eats)

food.update({'beans' : 1500})
print (food) 


food.copy()
print(food)


students ={1 : "Samson",
           2 : "Yaseen",
           4 : "Elton"}
print(students)

print(students[4])
print (students[1])
print(students.get (2))
print(students.get(3),"Not found")


list1 =["Samason","Yaseen","Elton"]
list2= [1,2,3]
dict10 = dict (zip (list2,list1))
print(dict10)
print(dict10.get(1))
print(dict10.get(10),"Not found.....")

dict_of_results= {'elton' : 7.5,
                  'yaseen': 10,
                  'samson':6.5
                  } 
print(dict_of_results)
for results in dict_of_results :
    print(results)
   
        


dictionary1 ={1 : "Samson",
              2: "Yaseen",
              3 : "Elton",
              }
print(dictionary1)
for new_dictionary in dictionary1:
    print(new_dictionary)
   











    








































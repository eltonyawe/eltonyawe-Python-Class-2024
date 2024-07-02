list_of_students = [["eto", "sam", "seen"],
                    ["martha", "tinah"],
                    [10000, 3.5]
                    ]
print(list_of_students)

print(list_of_students[2][1])
print(list_of_students[1])

for results in list_of_students :
    for marks in results:
        print(marks,end=" ")

    print()        

Num_pad =[[1,2,3,],
          [4,5,6],
          [7,8,9],
          ["*",0,"#"]]
print(Num_pad)
for loop in Num_pad :
    for Num_pad_og in loop :
        print(Num_pad_og,end=" ")
    print()

pythonclass = [['eto','sam','yaseen'],
               ['martha','caroll'],
               ['tonny','miss']]
print(pythonclass)
for names in pythonclass:
    for students in names:
        print(students,end = " ")
        print()  

items1 =      [['mangoes','oranges','grapes'],
               ['carrots','nakati','cabbage'],
               ['beef','chicken']]
print(items1)


print(items1[2])
print('Before Update')
print(items1[1][1])

#How to update a list/array
print('After Update')
(items1[1][1]) = 'greens'

print(items1[1][1])

#How add a list to a 2Dlist
food = ['potatoes','rice','chapati']
menu = items1,food

a=[["eto","yaseen","samson"],
   ["martha","tonny"],
   [7.5,10,6.7],
   [100,10000]]
print(a)
for numb in a:
    for number in numb:
        print(number,end=' ')
    print()    


#How to add items in a dictionary
dict_of_results= {'elton' : 7.5,
                  'yaseen': 10,
                  'samson':6.5
                  } 
print("before adding item")
print(dict_of_results)

print("after adding item")
dict_of_results["martha"] = 8
print(dict_of_results)
    
#A Switch Case ....
#example1

def switch (value) :
    return dict_of_results.get(value,42)

print (switch ('value'))  


#How to implement switch case in dictionaries
dict_of_results= {'elton' : 7.5,
                  'yaseen': 10,
                  'samson':6.5
                  } 
print(dict_of_results)


def switch (value) :
    return dict_of_results.get(value,42)
print (switch ('elton'))
print(switch('yaseen'))
print(switch('samson'))
print(switch('unknown'))


 


      



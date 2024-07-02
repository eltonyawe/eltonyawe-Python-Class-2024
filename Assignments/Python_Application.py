#A List of Items
list_of_fruits = ['mangoes','apples','oranges','grapes']
print('Original list before Editing...')
print(list_of_fruits)


#Join function() it combines list items a one 
print('List after being Joined {''each word joined to the next line''}')
print('\n'.join (list_of_fruits))
#joined using double udderscore
print('List after being Joined {''each word joined with a double udderscore''}')
print('__'.join (list_of_fruits))



#find function() it finds the location of a character in a string 
people = 'list of people'
print(people)
print('index found')
new_peolpe = people.find('o')
print(new_peolpe)


#Replace function() it replaces an old item with a new one
name = "Tonny_Elton"
print('Name before Replacing...')
print(name)
print('Name after Replacing...')
replaced_name = name.replace("Elton","Stark")
print(replaced_name)



#Split function() it converts astring into multiple items of a list
msg = 'meats-veggies-fruits'
print('before splitting')
print(msg)
print('after splitting')
split_msg = msg.split('-')
print(split_msg)


#Dictionary 
dict_of_countrties = {"Uganda"  : "Kampala",
                      'Kenya'   : 'Nairobi',
                      'Tazania' : 'Mombasa',
                      'Rwanda'  : 'Kigali'
                      }
                      
print('Original Dictionary of Counties before Editing...')
print(dict_of_countrties)


#Join function()
print('Dictionary Joined with dushes')
print('--'.join(dict_of_countrties))
print('Dictionary Joined with next line')
print('\n'.join(dict_of_countrties))


#Replace function()
country = '''Uganda : Kampala'''
print('before replacing...')
print(country)
new_country = country.replace('Kampala','London')
print('After Replacing..')
print(new_country)


#NB: find,split,replace are not dictionary or list in built funtions
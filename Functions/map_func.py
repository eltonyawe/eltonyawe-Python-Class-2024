
#map(function,iterable)
#join
lst = ['Hello World','How are you']
joined_lst = "\n".join(lst)
print(joined_lst)

#split
s = 'Hello-World'

split_s = s.split("-Wo")
print(split_s)

#Strip
s = '%Hello World%'
print(s)
stripped_s = s.strip('%')
print(stripped_s)


a = 1500 
b = 900
c = 1000
d = 500
def discount(a,b,c,d):

    if a >= 1000 :
        print("Discount Allowed")
    elif b <= 1000:
        print('Discount Not allowed')
    elif c == 1000:
        print('Perfect Discount') 
    elif d < 500:
        print('Not Allowed')
    else:
        print('Not Allowed at all')       
    
    
print(discount(1500,900,1000,100))

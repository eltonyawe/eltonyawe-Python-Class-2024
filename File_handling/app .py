# 'w' = write
# 'r'= read
# 'a' = append
# 'x' = create

# read - pints error if file doesnot exist

f = open('data.txt','r')
print(f.read())
f.close()

# Read line / lines in file handling 
f = open('data.txt','r')
print(f.readlines())
f.close()


#Write to a file 
file = open('data.txt','w')
print(file.write('Python in A.I'))
file.close()

#Append to a file
file = open('data.txt','a')
print(file.write('Python in A.I'))
file.close()


#Using with in file handling
with open('data.txt','a') as file1:
    print(file1.write("1st new sentence :i love programming"))
    print(file1.write("2nd new sentence :i love A.I"))
    



import json

def read_json_file(filename):
    with open(filename,'r') as file:
        data = json.load(file)
        return data
    

def write_json_file(data,filename):
    with open(filename,'w') as file:
       data1= json.dump(data,file,indent=2)
       return data1
   
filename = "Files/users.json"    
json_read_data=read_json_file(filename)
new_info ={
    "ID":0000,
    "Name" : "Homebase",
    "Age" : "23"
    
}

json_read_data.append(new_info) 
write_json_file(json_read_data,filename)
print(read_json_file(filename))

    
    
    
    
    
    

    
    
   
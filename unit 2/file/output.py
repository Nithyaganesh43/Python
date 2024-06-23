f1=open("student_data","r")
lines=len(f1.readlines())
f1.seek(0)
for i in range(lines):
    std=str(f1.readline())
    name,roll=std.split("|",1)
    print("Name :",name,end='')
    sp=" "
    print(sp*(20-len(name)),end='')
    print("Roll : ",roll)
    
        
                
            
    
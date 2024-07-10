d={"p":100,"s":50,"k":58 ,"r":65,"t":85}
name=input("enter name :")
print(d[name] if name in d.keys() else "not found" )
print("number of students mark<60 :",len(list(filter((lambda x: x>60 ),list(d.values())))))
print("Lowest mark students : ",[x for x,y in d.items() if y<=min(list(d.values()))][0])
f1=open("student_data","w")
n=int(input("No of students :"))
for i in range(n):
    name=input("\nEnter student name:")
    f1.write(name)
    f1.write("|")
    roll=input("\nEnter roll no :")
    f1.write(roll)
    f1.write("\n")
    
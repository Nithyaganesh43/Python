# print("pooja">"na")
# age=18
# if(age>100):
#     print("sethuta")
# elif(age<100 and age > 1 ):
#     print("iruka")
# else:
#     print("ava porakavey ila")
# def say():
#     return "adangommal"
# print(say())
def myfunc(n):
    print("my name is function")
    return lambda a : a * n
mydoubler = myfunc(2)#lambda a:a*2
mytripler = myfunc(3)#lambda a:a*3
print(mydoubler(11))
print(mytripler(11))
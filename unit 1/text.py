# # # # squares = []
# # # # for x in range(10):
# # # #     squares.append(x**2)
# # # # print(squares)

# # # # squares = [x**2 for x in range(10)]
# # # # print(squares)

# # # # lis = [f"{i} is Even number" if i % 2 == 0 else f"{i} is Odd number" for i in range(8)] 
# # # # print(lis) 

# # # l1 = ["eat", "sleep", "repeat"]
# # # s1 = "geek"

# # # # creating enumerate objects
# # # obj1 = enumerate(l1)
# # # obj2 = enumerate(s1)

# # # print ("Return type:", type(obj1))
# # # print (list(enumerate(l1)))

# # # # changing start index to 2 from 0
# # # print (list(enumerate(s1, 2)))
# # # for x,y in enumerate(name[2:5]):
# # #     print(x,y)
# # # name="poojana"
# # # print(name[:0])


# # # variable number of arguments
# def sum_numbers(a,*args):
#     """
#     Sums all numbers provided as arguments.
#     """
#     total = 0
#     for num in args:
#         total += num
#     return total

# # Calling the function with variable number of arguments
# result = sum_numbers(1, 2, 3, 4, 5)
# print("Sum:", result)  # Output: Sum: 15



# # # var keyword argument
# # def student_details(name, age, **kwargs):
# #     print(f"Name: {name}, Age: {age}")
# #     for key, value in kwargs.items():
# #         print(f"{key}: {value}")

# # student_details("Alice", 20, major="Computer Science", gpa=3.8)
# import math
# print(math.ceil(-10.5))
# a="i am the good boy"
# a=a.split()
# a="@".join(a)
# a=[x for x in a if x not in "hbvhvhbv"]
# a="".join(a)
# a=a.split('@')
# a=" ".join(a)
# print(a)
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))
tuple_constructor = tuple(thistuple)
print(tuple_constructor)

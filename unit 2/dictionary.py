# dic={}
# print(dic)
# dic[1]='poojana'
# dic[2]='elangovan'
# print(dic)
# print(len(dic))
# d=dic.copy()
# d[1]='bowya'
# print(dic,d)
# print(d.items())
# print(d.keys(),d.values())
# print(d.pop(2))
# print(d.get(1))
# d[2]=dic[1]
# dic.clear()
# del d,dic
# print(dic)
dict_c = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# # Iterating through keys
# for key in dict_c:
#     print(key, dict_c[key])

# # # # Iterating through values
# for value in dict_c.values():
#     print(value)

# # # # Iterating through key-value pairs
for key, value in dict_c.items():
    print(key, value)

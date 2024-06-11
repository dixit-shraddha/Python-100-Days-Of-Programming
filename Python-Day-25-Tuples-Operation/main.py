tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)
# res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)

tup = ("string",1,2,3,True)
print(type(tup))
print(tup, "\n" )


list_1 = list(tup)
print(type(list_1))
print(list_1)

list_1.append("new")
print(list_1)

tup = tuple(list_1)
print(tup)

print(tup.count("string"))
print(tup.count("True")) #consider true as string
print(tup.count(True)) # consider true as 1 hence count is 2
print(tup.index(2))
print(tup.index("string"))
print(len(tup))
print(tup.index(True,2,5))

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
#res = tuple1.count(3)
#res = tuple1.index(3)
# res = tuple1.index(311)
res = tuple1.index(3, 4, 8)
#res = len(tuple1)
print('Count of 3 in tuple1 is:', res)

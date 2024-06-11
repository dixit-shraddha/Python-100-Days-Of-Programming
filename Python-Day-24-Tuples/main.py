tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)

# tup = (1,2,3,4,5,6,7,8,9,10)
# print(type(tup))
# tup1 = (1)
# print(type(tup1))

# tup2 = (1,)
# print(type(tup2))

tup3 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tup3[0])
print(tup3[1])
print(tup3[-1])
print(tup3[-2])
print(tup3[1:4])
print(tup3[:4])
print(tup3[1:])
print(tup3[::2])
print(tup3[1:9:3])
print(tup3[0:9:3])
print(len(tup3))

if 3 in tup3:
  print("Yes")
else:
  print("No")

tup5 = tup3[1:4]
print(tup5)

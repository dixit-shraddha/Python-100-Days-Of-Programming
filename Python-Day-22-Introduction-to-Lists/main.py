li_1 = [1,2,3,4,5]
li_2 = ['a','b','c']
li_3 = [1,2,'a',True]

print(li_1)
print(li_2)
print(li_3)

for i in li_1 :
  print(i)

print("\n")
print(li_1[2])
print(li_1[-2])
print(li_1[1:3])
print(li_1[:])
print(li_1[:-1])

if 2 in li_1 :
  print("yes")
else:
  print("No")

if 'y' in li_2:
  print("yes")
else:
  print("no")


li_4 = [1,2,3,4,5,6,7,8,9,10]
print(li_4)
print(li_4[0:10:2])

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
nameswith_a = [item for item in names if "a" in item]
print(nameswith_a)
namesWith_1 = [item for item in names if (len(item) > 4)]
print(namesWith_1)


marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

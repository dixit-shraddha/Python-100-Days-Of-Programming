# The method related to sets are:-
# 1) union()---->creates a new set with the unique elements from both the sets
# 2)update()----->applied on a set itself and it also adds unique elements from the both the sets into one of the sets
# 3) intersection()----> creates a new set with the common elements from both the sets
# 4)intersection_update()------> applied on a set itself and it also contains the common elements from both the sets
# 5)symmetric_difference--------> creates a new set with the elements from the both the sets that are not common in between
# 6)symmetric_difference_update-------> applied on a set itself and it contains elements from the sets that are not common inj between
# 7)difference------> creates a new set with the elements from a single set that are not common 
# 8) difference_update-----> applied on a set itself and contains elements of a set that are not common

# 9)isdisjoint()---->checks if there are common elements between two sets
# 10)issuperset----> checks if a set is a superset of another set
# 11) issubset-----> checks is a set is subset of another set
# 12)add------> to add a element into a set
# 13) remove-------> to remove an elements from a set, but raises key error if the element is not present in the set
# 14) discard-----> to remove an element from a set, does not raises error if the lement is not present in the set
# 15) del------> not method, a keyword, to delete the complete set
# 16) clear-------> to clear all the elements of a set 
# 17) in keyword used to check if a element is present in the set or not
# 18) pop()-----> to remove a random element from the set and also we can get that element

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = {6, 7, 8}
print("set_1: ",set_1)
print("set_2: ",set_2)
print("set_3: ",set_3)

set_5 = set_1.union(set_2)
print("set_5: ",set_5)

set_1.update(set_2)
print("set_1: ",set_1)

set_4 = set_1.intersection(set_2)
print("set_4: ",set_4)

set_1.intersection_update(set_2)
print("set_1: ",set_1)

set_1 = {1, 2, 3}
print("set_1: ",set_1)

set_6 = set_1.symmetric_difference(set_2)
print("set_6: ",set_6)

set_1.symmetric_difference_update(set_2)
print("set_1: ",set_1)

set_1.difference(set_2)
print("set_1: ",set_1)

set_1.difference_update(set_2)
print("set_1: ",set_1)

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = {6, 7, 8}
print(set_1.isdisjoint(set_2))
print(set_1.isdisjoint(set_3))
print(set_1.issuperset(set_2))
print(set_1.issubset(set_2))

set_1 = {1,2,3,4,5,6,7,8,9}
print(set_1.issuperset(set_2))
print(set_2.issuperset(set_1))

print(set_1.issubset(set_2))
print(set_2.issubset(set_1))

set_1 = {1,2,3,4,5,6,7,8,9}  
set_1.add(10)
print("set_1: ",set_1)

set_1.remove(10)
print("set_1: ",set_1)

set_1.discard(9)
print("set_1: ",set_1)

del(set_1)
# print(set_1)

set_2.clear()
print(set_2)

print(set_3)
set_3.pop()
print(set_3)

set_1 = {1,2,3,4,5,6,7,8,9}

for i in set_1:
  print(i)

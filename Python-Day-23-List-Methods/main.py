colors = ["voilet", "indigo", "blue", "green"]

print(colors)
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)

num = [4, 2, 5, 3, 6, 1, 2, 1, 2, 8, 9, 7]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4, 2, 5, 3, 6, 1, 2, 1, 2, 8, 9, 7]
num.reverse()
print(num)

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("indigo"))

num = [4, 2, 5, 3, 6, 1, 2, 1, 3, 2, 8, 9, 7]
print(num.index(3))

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

newlist = colors.copy()
print(newlist)
newlist.append("red")
print(newlist)
newlist.insert(1, "orange")
print(newlist)
colors.extend(num)
print(colors)
print(colors + num)


l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))
# print(l.count(1))
# m = l.copy()
# m[0] = 0
# l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m
# print(k)
# l.extend(m)
print(l)

import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
# print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!")

import time
hour = int(time.strftime('%H')) + 6
print(hour)
# t = time.strftime('%H:%M:%S')
# print(t)

if (hour >=0 and hour <12):
  print("Good Morning")
elif (hour >=12 and hour <15):
  print("Good Afternoon")
elif (hour >= 15 and hour <17):
  print("Good Evening")
else:
  print("Good Night")

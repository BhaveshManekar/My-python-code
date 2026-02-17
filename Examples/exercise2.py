import time
t= time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
#hour= int(input("enter hours:"))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<18):
    print("Good Afternoon Sir!")
elif(hour>=18 and hour<24):
    print("GOOD Night Sir!")
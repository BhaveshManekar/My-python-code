#break statement
for i in range(12):
    if (i==10):
     break
    print("5 X",i+1,"=",5*(i+1))
print("skip the loop")

#continue statement
for i in range(13):
   if(i==11):
      continue
   print("5 X",i+1,"=",5*(i+1))

# #do while
# i=0
# while True:
#    print(i)
#    i = i+1
#    if (i%100 == 0):
#       break   
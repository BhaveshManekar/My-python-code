marks =[21,25,64,95,97,39,61]
# this is an simple exmple
index =0
for mark in marks:
    print(mark)
    if (index ==3):
        print("good")
    index +=1

# enu fun is build in fun in python.
# that allows you to loop over a sequence and get the index and value 
for index, mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("good")

# to start form start 
for index, mark in enumerate(marks,start=1):
    print(mark)
    if(index==3):
        print("good")

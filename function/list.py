marks=[2,4,5,9,"bhavesh",True,6,4,5,75,1,2,1,9]
print(marks)
# print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
print(marks[-3])
print(marks[len(marks)-3])

if 7 in marks:
    print("yes")
else:
    print("no")

print(marks)
print(marks[:])
print(marks[0:8:3])

lst=[i for i in range(8)]
print(lst)
lst=[i*i for i in range(8) if i%2==0]
print(lst)
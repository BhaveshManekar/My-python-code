# Tuples are ordered collection of data items.
# tuples are unchangable meaning we cannot change them after creation.
# tup=(1) we dont write that in tuple tup=(1,)
tup=(1,3,4,5,67,3,94,"green", True)
print(type(tup),tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[-3])

if 97 in tup:
    print("yes it is present")
else:
    print("not present")

tup2=tup[1:4]
print(tup2)

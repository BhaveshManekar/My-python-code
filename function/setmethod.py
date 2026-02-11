# Union and  Union_update()
s1={1,2,3,4,5,6}
s2={5,6,7,8}
# print(s1.union(s2))
s1.update(s2)
print(s1,s2)

#intersection and intersection_update()
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities.intersection(cities2)
cities.intersection_update(cities2)
print(cities)

# Symmetric difference and symmetric_difference_update()
# the values which is not common
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities.symmetric_difference(cities2)
print(cities3) 

# Difference() and Difference_update()
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities.difference(cities2)
print(cities3) 

# isdisjoint()
# both the sets are different
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
print(cities.isdisjoint(cities2))

# issuperset()
if c2 element are present in c1 the it is a superset 
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Madrid"}
print(cities.issuperset(cities2))

# add
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Madrid"}
print(cities.issuperset(cities2))

# update
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Madrid"}
cities.update(cities2)
print(cities)

# remove/discard
# diff is that when we remove the item which is not present in set,
# remove raise an error, whereas discard does not raise and error.
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities.remove("Tokyo")
print(cities)

cities={"Tokyo","Madrid","Berlin","Delhi"}
cities.discard("Tokyo")
print(cities)

# pop() this method removes the last item of the set bud the catch is that we don't know which item gets popped as set are unordered.
cities={"Tokyo","Madrid","Berlin","Delhi"}
item=cities.pop()
print(cities)
print(item)

# del is not a method,rether it is a keywoed which delets the set entirely.
cities={"Tokyo","Madrid","Berlin","Delhi"}
del cities
# print(cities)

# check if item exists
info = {"Carla",19,False,5.9}
if "Carla"in info:
    print("Carla is present.")
else:
    print("Carla is absent.")








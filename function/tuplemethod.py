# countries = ("Spain","Italy","India","England","Germany")
# temp=list(countries)
# temp.append("Russia")     #add item
# temp.pop(3)               #remove item
# temp[2]="Finland"         #change item
# countries=tuple(temp)
# print(countries)

# countries =("India","Afghanistan","Bangladesh","shrilanka")
# countries2=("vietnam","china","Rassia")
# Asia= countries + countries2
# print(Asia)

tuple1 = (0,1,2,3,4,3,5,6,7,3,8,1,9,3)
# res = tuple1.count(3)
# res = tuple1.index(3)
res = tuple1.index(3,4,8)    #it find 3 in between the index 4 to 8
res=len(tuple1)
print("count of 3 in tuple1 is:",res)
l=[11,69,5,8,1,11,15,64,27,1]
print(l)
# add 7 to the last
l.append(7)
# arrange the data in assending order 
l.sort()
# arrange the data in decending order
l.sort(reverse=True)
# reverse the list
l.reverse()
# print the index 1
print(l.index(1))
# print the coune of index one
print(l.count(1))
m= l.copy()
m[0]=0
# insert the 899 on index 1
l.insert(1,899)
m=[900,100,1100]
k=l+m
print(k)
# extend the l to m
l.extend(m)
print(l)

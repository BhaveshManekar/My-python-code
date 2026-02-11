Dictionaries are ordered colloction of data items.they store multiple items in a single variable.
dic ={
   "bhavesh":"human being",
   "spoon" : "object"
}
print(dic["bhavesh"])

dic2 = {
   125:"bhavesh", 
   845:"mahesh" ,
   194:"prathmesh", 
   128:"himesh" 
}
print(dic2[194])

info={"Name":"Bhavesh","age":23,"eligible":True}
print(info)
print(info["Name"]) # it show the error
print(info.get("eligible")) #it does not show the erreo it show "none"

for keys
info={"Name":"Bhavesh","age":23,"eligible":True}
print(info)
print(info.keys())

for key in info.keys():
    print(info[key])

for values
info={"Name":"Bhavesh","age":23,"eligible":True}
print(info)
print(info.values())

for key in info.keys():
    print(f"The value corresponding to the key{key} is {info[key]}")

info={"Name":"Bhavesh","age":23,"eligible":True}
print(info.items())
for key in info.keys():
    print(f"The value corresponding to the key{key} is {info[key]}")
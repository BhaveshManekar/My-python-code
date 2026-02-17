# Dictionaries are ordered colloction of data items.they store multiple items in a single variable.
# First dictionary
dic = {
    "bhavesh": "human being",
    "spoon": "object"
}
print(dic["bhavesh"])

# Second dictionary
dic2 = {
    125: "bhavesh",
    845: "mahesh",
    194: "prathmesh",
    128: "himesh"
}
print(dic2[194])

# Dictionary info
info = {"Name": "Bhavesh", "age": 23, "eligible": True}
print(info)
print(info["Name"])          # correct key
print(info.get("eligible"))  # safe method

# Loop through keys
print(info.keys())
for key in info.keys():
    print(info[key])

# Loop through values
print(info.values())
for value in info.values():
    print(value)

# Loop with formatted output
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

# Using items()
print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

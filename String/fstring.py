letter = "MY name is {1} and I am form {0}"
name = "Bhavesh"
country = "India"

# print(letter.format("India","Bhavesh"))

print(f"MY name is {name} and I am form {country}")

# it only the 2 digit after the decimal point 
price=45.3215
txt=f"for only{price:.2f}dollars"
# print(txt.format())
print(txt)

print(f"{2*30}")

# to see the curly bracket we have to do this 
print(f"MY name is {{name}} and I am form {{country}}")
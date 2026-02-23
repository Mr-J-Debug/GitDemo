# counting substring from a string
# count()
# string.count(substring)
s1 = "we are learning python, python is fun"
s2 = "python"
print(s1.count(s2))
s3 = "e"
print(s1.count(s3))
print (f" occurrences of {s2} is {s1.count(s2)}")

# change case of a string
# upper (), lower(), title(), capitalize()
s4 = "we are learning python 3.13"

print(s4.upper())
print(s4.lower())
print(s4.title())
print(s4.capitalize())

# startwith()
# string.startswith(substring)
print(s1.startswith("we"))
print(s1.startswith("We"))
print(s1.startswith("we are"))
print(s1.startswith("python"))

# endswith()
# string.endswith(substring)
print(s1.endswith("fun"))   
print(s1.endswith("Fun"))
print(s1.endswith("python"))

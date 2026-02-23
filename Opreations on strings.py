# s1 = "Python is fun"
# print(s1[0])
# print(s1[-1])
# print(len(s1))

# language = "Python"
# version = 3.8
# print(language + " " + str(version))
# membship operators
# in
# s1 = "Python is fun"
# print("is" in s1)
# print("are" in s1)
# # not in
# print("is" not in s1)   
# print("are" not in s1)  
# comparison of strings
print ("Python" == "Python")
# Remove spaces from the beginning and end of the string is called stripping/strip
s1 = "   Python"
s2 = "Python   "
s3 = "python"   
print(s1.strip())
print(s2.strip())
print(s1.lstrip())
print(s2.rstrip())  
print(s1.strip() == "Python")
# replace()
s1 = "we are learning Python" 
# s2 = s1.replace("Python", "Java")
print(s1)
# print(s2)
print(s1.replace("Python", "Java"))
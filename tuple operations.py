"""
concatenation, repetition, membership
count, index
min, max, sum
"""
student_detials1 = (1001, "John")
student_detials2 = (78.5,91.0,83.5,79.5)

# + = concatenation

student_detials = student_detials1 + student_detials2
print(student_detials)

# * = repetition
t1 = ("Class 5", 5000)
print(t1 * 3)

# in, not in = membership

print(91.0 in student_detials2)
print(99.0 in student_detials2)

print(91.0 not in student_detials2)
print(1001 not in student_detials1)

#  count()

t2 = (10,4,1,9,0,3,1)
# tuple.count(elements)
print(t2.count(1))

# index()
# tuple.index()
print(t2.index(4))
# min
# max
# sum
print(min(t2))
print(max(t2))
print(sum(t2))
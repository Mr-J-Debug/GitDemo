# Slicing of lists
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l1[1:6:1])
print(l1[1:6:2])
print(l1[1:6:3])

# Concatenation of lists
l2 = [11, 12, 13, 14, 15]
l3 = l1 + l2
print(l3)

# Repetition of lists
l4 = l1 * 3
print(l4)

# Append an element to the end of the list
# syntax: list.append(element)
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)

# Insert an element at a specific position
# syntax: list.insert(index, element)  
fruits.insert(1, 'grape')
print(fruits)



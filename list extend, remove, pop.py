"""extend()
remove()
pop()
"""
# extend() method is used to add multiple items to the end of a list.
list = ["apple", "banana", "cherry"]
list.extend(["orange", "grape"])
print(list)  # Output: ['apple', 'banana', 'cherry', 'orange', 'grape']

# remove() method is used to remove the first occurrence of a specified value from a list.
list = ["apple", "orange", "cherry", "banana"]
list.remove("banana")
print(list)  # Output: ['apple', 'orange', 'cherry']
# pop() method is used to remove and return an item at a given index from a list.
list = ["apple", "banana", "cherry"]
item = list.pop(1)   
print(item)  # Output: 'banana'
print(list)  # Output: ['apple', 'cherry']


# 
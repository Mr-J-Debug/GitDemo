"""
reverse()
sort()
count()
membership operatoin
"""
days_of_week = ["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days_of_week)
# reverse
days_of_week.reverse()
print(days_of_week)

nums =[4, 9, 0, 1, 2, 8]
print(nums)
# sort
nums.sort()
print(nums)
print("sorted list:", nums)
nums.sort(reverse=True)
print("sorted list:", nums)


# count
numbers = [0,1,2,3,4,1,0,5,0,0,3,0,0]
print(f"The list is: {numbers}")
item_to_count = int(input("Enter the number to be counted from the above list:"))
print(numbers.count(0))
c = numbers.count(item_to_count)
print(f"Occurrence of {item_to_count} is {c}")

# in
language = ["python","java","c++","Pythong"]
print("python" in language)

maths = ["python","java","alpha","beta","square"]
print("alpha" in maths)


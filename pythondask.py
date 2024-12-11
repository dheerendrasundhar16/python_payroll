#copy
vegetables = ["ladiesfinger", "drumstick", "tomato"]
vegetables.append("potato")
print(vegetables)
# Clear
vegetables = ["carrot", "potato", "tomato"]
vegetables.clear()
print(vegetables)

# Copy
vegetables = ["carrot", "potato", "tomato"]
x = vegetables.copy()
print(x)

# Count
vegetables = ["carrot", "potato", "tomato", "tomato"]
x = vegetables.count("tomato")
print(vegetables)

# Index
vegetables = ['carrot', 'potato', 'tomato']
x = vegetables.index("tomato")
print(x)

# Insert and Modify
a = [1, 2, 3, 4, 5, 6, 7, 8]
a.insert(6, 4)
a[3] = 5
print(a)

# Pop
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a.pop(2)
print(a)

# Extend
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 10, 11]
a.extend(b)
print(a)

# Append
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a.append(3)
print(a)

# Sort
vegetables = ['Cabbage', 'Carrot', 'Broccoli']
vegetables.sort()
print(vegetables)

#Remove
vegetables=['carrot','potato','tomato']
vegetables.remove("potato")
print(vegetables)

# Remove
vegetables = ['carrot', 'potato', 'tomato']
vegetables.remove("potato")
print(vegetables)

# Reverse
vegetables = ['carrot', 'potato', 'tomato']
vegetables.reverse()
print(vegetables)
list = [1, 2, 3, "four", 5.0]

# Access an element by index
print(list[2])  

# Add a new element to the list
list.append("six")
print(list)

# Remove an element by value
list.remove(2)

# Slice a list (get elements from index 1 to 3)
sliced_list = list[1:4]

# Loop through the list
for item in list:
    print(item)

# Check if an element exists in the list
if "six" in list:
    print("Found 'six'")



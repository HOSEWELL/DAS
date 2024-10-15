my_list = [1, 2, 3, 4, 5]

# Accessing elements by index
print(my_list[0])  

# Adding an element to the end of the list (array)
my_list.append(6)

# Removing an element by value
my_list.remove(3)

# Get the length of the list (array)
print(len(my_list)) 

# Looping through the list
for item in my_list:
    print(item)

# List slicing (getting a sub-array)
sub_list = my_list[1:3]  # Get elements from index 1 to 2 (exclusive of index 3)
print(sub_list)  

# Create a dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

# Access a value by its key
print(my_dict['name'])  # Output: John

# Add or update a key-value pair
my_dict['job'] = 'Engineer'

# Remove a key-value pair
my_dict.pop('age')

# Loop through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Check if a key exists
if 'city' in my_dict:
    print('City exists')

# Get the value for a key, return default if the key is not found
job = my_dict.get('job', 'No job found')

print(my_dict)

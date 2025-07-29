import json

python_dict = {
    "name": "Alice",
    "age": 30,
    "isStudent": False,
    "courses": ["Math", "Science"]
}

json_string = json.dumps(python_dict)

print(type(python_dict))  # Output: <class 'dict'>
print(python_dict)        # Output: {'name': 'Alice', 'age': 30, 'isStudent': False, 'courses': ['Math', 'Science']}

print(type(json_string))  # Output: <class 'str'>  #json string
print(json_string)        # Output: {"name": "Alice", "age": 30, "isStudent": false, "courses": ["Math", "Science"]}


#####################################################################################################################

import json

json_string = '{"name": "Bob", "age": 25, "city": "New York"}'

python_dict = json.loads(json_string)

print(type(json_string))  # Output: <class 'str'>
print(json_string)        # Output: {"name": "Bob", "age": 25, "city": "New York"}

print(type(python_dict))  # Output: <class 'dict'>
print(python_dict)        # Output: {'name': 'Bob', 'age': 25, 'city': 'New York'}

# You can now access elements of the dictionary:
print(python_dict['name']) # Output: Bob
print(python_dict['age'])  # Output: 25

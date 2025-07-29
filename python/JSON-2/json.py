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

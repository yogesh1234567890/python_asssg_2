"""18. Find a package in the Python standard library for dealing with
JSON. Import the library module and inspect the attributes of the
module. Use the help function to learn more about how to use the
module. Serialize a dictionary mapping 'name' to your name and 'age'
to your age, to a JSON string. Deserialize the JSON back into
Python."""

import json
help(json)
my_dict={'name':'yogesh','age':'19'}
#serializing
serialized_value=json.dumps(my_dict)
print(type(serialized_value))
print(serialized_value)
#deserializing
unpacked = json.loads(serialized_value)
print(type(unpacked))
print(unpacked)
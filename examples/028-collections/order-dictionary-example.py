from collections import OrderedDict

# Create an empty OrderedDict
ordered_dict = OrderedDict()

# Add items to the OrderedDict
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

# Print the OrderedDict
print(ordered_dict)

# Access an item by key
print(ordered_dict['b'])

# Iterate over the OrderedDict
for key, value in ordered_dict.items():
    print(key, value)
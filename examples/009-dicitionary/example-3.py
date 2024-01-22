# Create a Harry Potter dictionary
harry_potter_dict = {
    "Harry Potter": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    "Hermione Granger": "Gryffindor"
}

# Display the dictionary
print(harry_potter_dict)

# Characters to add to the Harry Potter dictionary
add_characters_1 = {
    "Albus Dumbledore": "Gryffindor",
    "Luna Lovegood": "Ravenclaw"
}

# Merge dictionaries
harry_potter_dict.update(add_characters_1)

# Display the dictionary
print(harry_potter_dict)

# Use iterables to update a dictionary
add_characters_2 = [
    ["Draco Malfoy", "Slytherin"],
    ["Cedric Diggory", "Hufflepuff"]
]
harry_potter_dict.update(add_characters_2)

print(harry_potter_dict)

# Use iterables to update a dictionary
add_characters_3 = [
    ("Rubeus Hagrid", "Gryffindor"),
    ("Minerva McGonagall", "Gryffindor")
]
harry_potter_dict.update(add_characters_3)

print(harry_potter_dict)

for key, value in harry_potter_dict.items():
    print(f"The current key :: {key} and its value :: {value}.")
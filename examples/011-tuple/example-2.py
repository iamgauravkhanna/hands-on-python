# Creating an empty tuple
empty_tuple = ()
print("Empty Tuple:", empty_tuple)

# Creating a tuple with elements
fruits = ('apple', 'banana', 'orange')
print("Fruits Tuple:", fruits)

# Creating a tuple with different data types
mixed_tuple = (1, 'hello', 3.14, True)
print("Mixed Tuple:", mixed_tuple)

# Accessing elements using index
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing a tuple
subset_fruits = fruits[1:3]
print("Subset of fruits:", subset_fruits)

# Concatenating tuples
more_fruits = ('grape', 'kiwi')
all_fruits = fruits + more_fruits
print("All Fruits:", all_fruits)

# Repetition
repeated_fruits = fruits * 2
print("Repeated Fruits:", repeated_fruits)

# Finding the index of an element
index_of_banana = fruits.index('banana')
print("Index of 'banana':", index_of_banana)

# Count occurrences of an element
count_apple = fruits.count('apple')
print("Count of 'apple':", count_apple)
